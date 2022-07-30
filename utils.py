import random
import json
import os
from config import DATA_DIR


def N():
    return random.randint(10, 30) / 10.0


def save_json(data, dirname, fileName):
    dirPath = os.path.join(DATA_DIR, dirname)
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
    
    filePath = os.path.join(dirPath, fileName)
    with open(filePath, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

