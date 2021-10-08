
import os
import yaml


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



