import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileList = [
    'requirements.txt',
    'src/__init__.py',
    'src/prompt.py',
    'Mtest/model.ipynb',
    'Mtest/imageDetection.ipynb',
    'src/helper.py',
    'setup.py',
    'app.py',
    '.env'
]

for file in fileList:

    file = Path(file)
    filedir,filename = os.path.split(file)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'{filename} is created in directory {filedir}')
    
    if(not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, 'w') as f:
            pass
            logging.info(f'{filename} is created in directory {filedir}')
    else:
        logging.info(f'{filename} is already exists in directory {filedir}')

