import random
import json
import os
from pymongo import MongoClient
from config import *

client = MongoClient(MONGODB['HOST'], MONGODB['PORT'])
db = client[MONGODB['DB']]


def N():
    return random.randint(10, 30) / 10.0


def gen_dir_path(dirname):
    dirPath = os.path.join(DATA_DIR, dirname)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    return dirPath


def save_html(data, dirname="html", fileName=None):
    dirPath = gen_dir_path(dirname)
    filePath = os.path.join(dirPath, fileName)
    with open(filePath, "w") as f:
        f.write(data)


def save_json(data, dirname=None, fileName=None):
    dirPath = gen_dir_path(dirname)
    filePath = os.path.join(dirPath, fileName)
    with open(filePath, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def is_exist(id, topicName):
    count = db[topicName].count_documents({'id': id})
    return count > 0


def save_mongo(nodes, topicName):
    for node in nodes:
        if not is_exist(node["id"], topicName):
            print(node["id"])
            db[topicName].insert_one(node)
