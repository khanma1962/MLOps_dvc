
from posixpath import join
from src.utils.all_utils import read_yaml, create_dir, evaluate_matrix, save_reports
import argparse
import pandas as pd
import os
import joblib


def evaluate(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # save dataset in the local directory
    # create path to directory: artifacts/row_local_dir/data.csv
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']

    test_datafile_name = config['artifacts']['test']
    test_data_path = os.path.join(artifacts_dir,split_data_dir, test_datafile_name )

    test_data = pd.read_csv(test_data_path, sep=';')

    test_y = test_data['quality']
    test_x = test_data.drop('quality', axis=1)


    model_dir = config['artifacts']['model_dir']
    model_file = config['artifacts']['model_filename']
    model_path = os.path.join(artifacts_dir,model_dir, model_file)

    lr = joblib.load(model_path)

    predicted_val = lr.predict(test_x)
    rmse, mae, r2 = evaluate_matrix(test_y, predicted_val)
    scores = {'rmse': rmse, "mae": mae, "r2":r2}

    scores_dir = config['artifacts']['scores_dir']
    scores_dir_path = os.path.join(artifacts_dir,scores_dir)

    create_dir([scores_dir_path])

    scores_file = config['artifacts']['scores']
    scores_path = os.path.join(scores_dir_path, scores_file)

    save_reports(reports=scores, reports_path=scores_path)
   

if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    evaluate(config_path=parsed_args.config, params_path=parsed_args.params)




