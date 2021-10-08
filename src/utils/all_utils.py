
import os
import yaml
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
import json


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"dirctory created as {dir_path}")

def save_local_data(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"Data has been saved at {data_path} location")


def save_reports(reports: dict, reports_path: str, indentation=4):
    with open(reports_path , "w") as f:
        json.dump(reports, f, indent=indentation)
    print(f"Reports are saved at {reports_path}")


def evaluate_matrix(acutal_val, pred_val):
    r2   = r2_score(acutal_val, pred_val)
    rmse = np.sqrt(mean_squared_error(acutal_val, pred_val))
    mae  = mean_absolute_error(acutal_val, pred_val)
    return rmse, mae, r2



