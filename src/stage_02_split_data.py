
from posixpath import join
from src.utils.all_utils import read_yaml, create_dir, save_local_data
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split


def split_save_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # save dataset in the local directory
    # create path to directory: artifacts/row_local_dir/data.csv
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    df = pd.read_csv(raw_local_dir_path)
    test_size = params['base']['test_size']
    random_state = params['base']['random_state']

    train, test = train_test_split(df, test_size=test_size, random_state=random_state)

    split_data_dir = config['artifacts']['split_data_dir']
    train_datafile_name = config['artifacts']['train']
    test_datafile_name = config['artifacts']['test']

    create_dir([os.path.join(artifacts_dir,split_data_dir)])

    train_data_path = os.path.join(artifacts_dir,split_data_dir, train_datafile_name )
    test_data_path  = os.path.join(artifacts_dir,split_data_dir, test_datafile_name )
    
    for data, data_path in (train, train_data_path), (test, test_data_path):
        save_local_data(data, data_path)



if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    split_save_data(config_path=parsed_args.config, params_path=parsed_args.params)




