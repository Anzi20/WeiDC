# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import random
import json
import numpy as np
import torch
import torch.nn as nn
from pytorch_pretrained_bert.tokenization import BertTokenizer
from pytorch_pretrained_bert.file_utils import PYTORCH_PRETRAINED_BERT_CACHE

class Config(nn.Module): 
    def __init__(self, args):
        super().__init__()
        self.alpha = args.alpha  # balance factor
        self.max_seq_length = args.max_seq_length
        with open('./data/{}/tag.json'.format(args.data_name), 'r', encoding='utf-8') as fp:
            self.label2id = json.load(fp)
        self.id2label = {i:label for label, i in self.label2id.items()}
        self.num_labels = len(self.label2id) + 1  # We do not use 0

        # BERT
        self.output_model_dir = args.output_model_dir
        self.bert_model = args.bert_model
        self.cache_dir = args.cache_dir if args.cache_dir else str(PYTORCH_PRETRAINED_BERT_CACHE)
        

class Process(nn.Module): 

    def __init__(self, config):
        super().__init__()
        self.num_labels = config.num_labels
        self.label2id = config.label2id
        self.max_seq_length = config.max_seq_length
        self.tokenizer = BertTokenizer.from_pretrained(config.bert_model, do_lower_case=True)

    def load_data(self, data_path, do_predict=False):
        if not do_predict:
            flag = data_path[data_path.rfind('/')+1 : data_path.rfind('.')] 
            return self.readfile(data_path, flag)
        else:
            return self.readsentence(data_path)

    def convert_examples_to_features(self, examples):
        max_seq_length = min(max([len(e[0]) for e in examples])+2, self.max_seq_length)
        features = []
        
        for (tokens, labels) in examples:   
            if len(tokens) >= max_seq_length - 1:
                tokens = tokens[0:(max_seq_length - 2)]
                labels = labels[0:(max_seq_length - 2)]
            
            ntokens = []
            label_ids = []

            ntokens.append("[CLS]")
            label_ids.append(self.label2id["[CLS]"])

            for i, token in enumerate(tokens):
                token = self.tokenizer.tokenize(token)
                if len(token) == 0:
                    continue
                ntokens.extend(token)
                label_ids.append(self.label2id[labels[i]])
            
            ntokens.append("[SEP]")
            label_ids.append(self.label2id["[SEP]"])
            input_ids = self.tokenizer.convert_tokens_to_ids(ntokens)

            input_mask = [1] * len(input_ids)

            while len(input_ids) < max_seq_length:
                input_ids.append(0)
                label_ids.append(0)
                input_mask.append(0)
            
            assert len(input_ids) == max_seq_length
            assert len(label_ids) == max_seq_length
            assert len(input_mask) == max_seq_length

            features.append((input_ids, label_ids, input_mask))
        return features

    def feature2input(self, device, feature):
        input_ids = torch.tensor([f[0] for f in feature], dtype=torch.long).to(device)
        label_ids = torch.tensor([f[1] for f in feature], dtype=torch.long).to(device)
        input_mask = torch.tensor([f[2] for f in feature], dtype=torch.long).to(device)
        return input_ids, label_ids, input_mask

    def readfile(self, filename, flag):
        f = open(filename, 'r', encoding="utf-8")
        data = []
        sentence = []
        label = []
        
        for line in f:
            if len(line) == 0 or line.startswith('-DOCSTART') or line[0] == "\n":
                if flag == 'train':
                    if len(sentence) > 32 or (0 < len(sentence) <= 32 and np.random.rand(1)[0] < 0.25):
                        data.append((sentence, label)) 
                        sentence = []
                        label = []
                    continue
                else:
                    if len(sentence) > 0:
                        data.append((sentence, label))
                        sentence = []
                        label = []
                    continue
            splits = line.strip().split('\t')
            char = splits[0]
            l = splits[-1]
            sentence.append(char)
            label.append(l)
            if char in ['，', '。', '？', '！', '：', '；', '（', '）', '、'] and len(sentence) > 64:
                data.append((sentence, label))
                sentence = []
                label = []

        if len(sentence) > 0:
            data.append((sentence, label))
            sentence = []
            label = []
        return data

    def readsentence(self, filename):
        f = open(filename, 'r', encoding="utf-8")
        data = []
        sentence = []

        for line in f:
            line = line.strip().replace(' ', '')
            for char in line:
                sentence.append(char)
                if char in ['，', '。', '？', '！', '：', '；', '（', '）', '、'] and len(sentence) > 64:
                    label = ['S'] * len(sentence)
                    data.append((sentence, label))
                    sentence = []

            if len(sentence) > 0:
                label = ['S'] * len(sentence)
                data.append((sentence, label))
                sentence = []
        return data