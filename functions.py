import json


def read_json(file):
    with open(file, encoding="utf-8") as f:
        return json.load(f)


def get_tags(data):
    results = set()
    for i in data:
        content = i['content']
        words = content.split()
        for word in words:
            if word.startswith("#"):
                results.add(word[1:])
    return results
