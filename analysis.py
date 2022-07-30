from typing import List
import os
import json
from config import *


def parse_content(nodes: List):
    for node in nodes:
        print(node.get("content", ""))
        print("--" * 20)


def analysis():
    for topic in TOPIC_IDS:
        topicName, topicId = tuple(topic.items())[0]

        for i in range(MAX_PAGE):
            dirPath = os.path.join(DATA_DIR, topicName)
            rawDataFilePath = os.path.join(dirPath, f'raw_{i}.json')
            if not os.path.exists(rawDataFilePath):
                print("no content any more.")
                return
            with open(rawDataFilePath, "r") as f:
                rawData = json.load(f)
            
            nodes = rawData.get("data", {}).get("topic", {}).get("feeds", {}).get("nodes", [])
            parse_content(nodes)



if __name__ == "__main__":
    analysis()
