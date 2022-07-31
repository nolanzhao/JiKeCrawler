import json
import requests
import time
from datetime import datetime
from utils import N, save_json, save_mongo
from cookie_tools import init_cookie
from config import *


def retrive(lastId=""):
    PAYLOAD["variables"]["loadMoreKey"]["lastId"] = lastId
    r = requests.session()
    res = r.post(url="https://web-api.okjike.com/api/graphql", headers=HEADERS, data=json.dumps(PAYLOAD))
    # print(res.status_code)
    rawData = res.json()
    return rawData


def main():
    init_cookie()
    lastId = ""
    for topic in TOPIC_IDS:
        topicName, topicId = tuple(topic.items())[0]
        PAYLOAD["variables"]["topicId"] = topicId
        for i in range(MAX_PAGE):
            print(f"TOPIC: {topicName}  PAGE: {i}")
            rawData = retrive(lastId)
            if rawData is None:
                return
            # print(rawData)
            nodes = (((rawData.get("data", {}) or {}).get("topic", {}) or {}).get("feeds", {}) or {}).get("nodes", []) or []
            if len(nodes) == 0:
                return
            lastId = nodes[-1]["id"]
            save_json(rawData, topicName, f'raw_{i}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}.json')
            save_mongo(nodes, topicName)
            time.sleep(N())


if __name__ == "__main__":
    main()
