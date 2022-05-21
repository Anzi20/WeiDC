# WeiDC

This is the implementation of [Weighted self Distillation for Chinese word segmentation](https://aclanthology.org/2022.findings-acl.139/) at [Findings of the Association for Computational Linguistics: ACL 2022](https://aclanthology.org/volumes/2022.findings-acl/).

## Requirements

Our code works with the following environment.
* `python=3.6.13`
* `pytorch=1.7`

## Downloading BERT or RoBERTa

In our paper, we use BERT ([paper](https://www.aclweb.org/anthology/N19-1423/)), please download pre-trained BERT-Base Chinese from [Google](https://github.com/google-research/bert) or from [HuggingFace](https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz). You can also choose RoBERTa from [roberta_zh](https://github.com/brightmart/roberta_zh).

## Datasets

We use [SIGHAN2005](http://sighan.cs.uchicago.edu/bakeoff2005/) in our paper.

To obtain pre-processed data, please follow [Improving  Chinese  Word  Segmentation  with  Wordhood  Memory  Networks](https://www.aclweb.org/anthology/2020.acl-main.734/). 

Furthermore, we conduct some NER tasks (including `WEIBO`, `RESUME`, and `MSRA`).

# The WeiDC

For AttenCD, you can download our codes to train models.

***You can find the command lines to train and test models on a specific dataset in `run.sh`.***

## Training

Here are some important parameters:

* `--do_train`: training mode.
* `--num_wei`(num_atten): weight class.
* `--ratio`: control the amount of training data.
* `--data_name`: the name of the data to be trained.
* `--dict_path`: the dictionary path.
* `--bert_model`: the directory of pre-trained BERT or RoBERTa model.
* `--model_name`: the name of model to save.

## Testing

Here are some important parameters:

* `--do_test`: testing mode.
* `--test_model`: the pre-trained AttenCD model.
* `--data_name`: the name of the data to be tested.
* `--dict_path`: the dictionary path.

## Predicting

note: Only the prediction method of CWS task is implemented.

Here are some important parameters:

* `--do_predict`: predicting mode.
* `--input_file`: the file to be predicted.
* `--output_file`: the path of the output file.
* `--test_model`: the pre-trained AttenCD model.

# Citation
If you use or extend our work, please cite our paper at ACL2022. [bibtex](https://dblp.org/rec/conf/acl/HeC0Z22.html?view=bibtex)
```
@inproceedings{DBLP:conf/acl/HeC0Z22,
  author    = {Rian He and
               Shubin Cai and
               Zhong Ming and
               Jialei Zhang},
  editor    = {Smaranda Muresan and
               Preslav Nakov and
               Aline Villavicencio},
  title     = {Weighted self Distillation for Chinese word segmentation},
  booktitle = {Findings of the Association for Computational Linguistics: {ACL} 2022,
               Dublin, Ireland, May 22-27, 2022},
  pages     = {1757--1770},
  publisher = {Association for Computational Linguistics},
  year      = {2022},
  url       = {https://aclanthology.org/2022.findings-acl.139},
  timestamp = {Thu, 19 May 2022 16:52:59 +0200},
  biburl    = {https://dblp.org/rec/conf/acl/HeC0Z22.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

# others
You can leave comments in the `Issues` section, if you have any questions about our methods.
