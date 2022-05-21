mkdir logs

# ner test
CUDA_VISIBLE_DEVICES=0 python main.py --do_train --num_wei=1 --ratio=1.0 --data_name=weibo --model_name=weibo_test --bert_model=./pretrained_models/bert-base-chinese/