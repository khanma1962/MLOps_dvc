# dvc-ML-demo-AIOps
This is the flow we are following for this course


![MLOPs_dvc](https://github.com/khanma1962/MLOps_dvc/blob/main/dvc_ML.png)


### Step 1 - Create an empty repository

### Step 2 - Intitialize the repository

echo "# dvc-ML-demo-AIOps" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/USER_NAME/REPO_NAME.git
git push -u origin main


touch .gitignore


### Step 3 - Create conda env

conda create --name mlops python=3.7 
conda activate mlops



### Step 4 - Create a setup file

touch setup.py

paste the following text
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="USER_NAME",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c17hawke/dvc-ML-demo-AIOps",
    author_email="sunny.c17hawke@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)


### Step 5 - Create and install dependencies

touch requirements.txt
pip install -r requirements.txt


### Step 6 - intitialize dvc

dvc init


### Step 7 - Create the basic directory structure

mkdir -p src/utils config


### Step 8 - Create the basic directory structure

touch config/config.yml

add the following text
data_source: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

artifacts: 
  artifacts_dir: artifacts
  raw_local_dir: raw_local_dir
  raw_local_file: data.csv


### Step 9 - Create the stage 01 python file and all_utils_file

touch src/stage_01_load_save.py src/utils/all_utils.py


### Step 10 - Create the dvc.yaml file and add stage 01

touch dvc.yaml

add this in the dvc.yaml file
stages:
  load_data:
    cmd: python src/stage_01_load_save.py --config=config/config.yaml
    deps:
      - src/stage_01_load_save.py
      - src/utils/all_utils.py
      - config/config.yaml
    outs:
      - artifacts/raw_local_dir/data.csv


### Step 11 - run the dvc command

dvc repro

### Step 12 - Push the changes to the remote repository

git add .
git commit -m "stage 01 added"
git push origin main



