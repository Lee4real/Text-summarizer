import os
import pathlib
import logging


logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'textSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/confing/__init__.py',
    f'src/{project_name}/confing/config.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'requirements.txt',
    'setup.py',
    'Dockerfile',
    'notebooks/trials.ipynb',
    'tests/test.py',

] 

for file in list_of_files:
    path = pathlib.Path(file)
    if path.exists():
        logging.info(f'{path} already exists')
    elif path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        logging.info(f'File created: {path}')
    else:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f'Directory created: {path}')