from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_decription = f.read()

setup(
    name='src',
    version='0.0.1',
    author='Moe',
    description='A small package for ML Pipline',
    long_decription=long_decription,
    long_decription_content_type='text/markdown',
    url="https://github.com/khanma1962/MLOps_dvc",
    author_email='khan_m_a@hotmail.com',
    package=['src'],
    python_requires='>3.7',
    install_requires=[
        'pandas',
        'dvc',
        'scikit_learn'
    ]

)