# WeiDC

This is the implementation of [?](?) at ?.

Please contact us at `?` if you have any questions.

## Requirements

Our code works with the following environment.
* `python=3.6`
* `pytorch=1.7`

## Downloading BERT and WeiDC

In our paper, we use BERT ([paper](https://www.aclweb.org/anthology/N19-1423/)), please download pre-trained BERT-Base Chinese from [Google](https://github.com/google-research/bert) or from [HuggingFace](https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese.tar.gz).

For WeiDC, you can download our codes to train models.


## Datasets

We use [SIGHAN2005](http://sighan.cs.uchicago.edu/bakeoff2005/) in our paper.

To obtain pre-processed data, please follow [Improving  Chinese  Word  Segmentation  with  Wordhood  Memory  Networks](https://www.aclweb.org/anthology/2020.acl-main.734/). 

## Training

You can find the command lines to train and test models on a specific dataset in `run.sh`.

Here are some important parameters:

* `--do_train`: train the model.
* `--do_test`: test the model.
* `--do_predict`: predict by  model.
* `--bert_model`: the directory of pre-trained BERT model.
* `--model_name`: the name of model to save.

## Testing

`test.sh`

Here are some important parameters:

## Predicting

`predict.sh`

Here are some important parameters:

* `--do_predict`: 
* `--input_file`: 
* `--output_file`: the path of the output file.
* `--test_model`: the pre-trained WeiDC model.

## others
You can leave comments in the `Issues` section, if you have any questions about our methods.
