mkdir logs

### --ratio
### --alpha
### --patience
### --num_wei
### --use_last
### --bert_model

# train
CUDA_VISIBLE_DEVICES=3 python main.py --do_train --ratio=1.0 --data_name=pku --dict_path=./data/pku/pku_dict.pkl --model_name=pku_base --patient=3

CUDA_VISIBLE_DEVICES=3 python main.py --do_train --num_wei=0 --ratio=1.0 --data_name=pku --dict_path=./data/pku/pku_dict.pkl --model_name=pku_na0 --patient=3 --alpha=0.3

CUDA_VISIBLE_DEVICES=3 python main.py --do_train --num_wei=4 --ratio=1.0 --data_name=pku --dict_path=./data/pku/pku_dict.pkl --model_name=pku_na4 --patient=3 --alpha=0.3

# # test
# CUDA_VISIBLE_DEVICES=3 python main.py --do_test --test_model=./path to model/model.pt --data_name=pku --dict_path=./data/pku/pku_dict.pkl

# # predict
# CUDA_VISIBLE_DEVICES=3 python main.py --do_predict --input_file=./path to data/xxx.txt --output_file=./path to output_file --test_model=./path to model/model.pt
