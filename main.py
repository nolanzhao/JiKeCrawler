
import json
from utils import save_json
import requests
import time
from utils import N
from config import *


def retrive(lastId=""):
    PAYLOAD["variables"]["loadMoreKey"]["lastId"] = lastId
    r = requests.session()
    res = r.post(url="https://web-api.okjike.com/api/graphql", headers=HEADERS, data=json.dumps(PAYLOAD))
    # print(res.status_code)
    rawData = res.json()
    return rawData



def main():
    lastId = ""
    for topic in TOPIC_IDS:
        topicName, topicId = tuple(topic.items())[0]
        PAYLOAD["variables"]["topicId"] = topicId
        for i in range(MAX_PAGE):
            print(f"TOPIC: {topicName}  PAGE: {i}")
            rawData = retrive(lastId)
            if rawData is None:
                return
            nodes = rawData.get("data", {}).get("topic", {}).get("feeds", {}).get("nodes", [])
            if nodes is None or len(nodes) == 0:
                return
            lastId = nodes[-1]["id"]
            save_json(rawData, topicName, f'raw_{i}.json')
            time.sleep(N())

    

    



if __name__ == "__main__":
    main()
