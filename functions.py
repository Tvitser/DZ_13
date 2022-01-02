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

def get_posts_by_tag(data, tag):
    results=[]
    for record in data:
        if f'#{tag}' in record["content"]:
            results.append(record)
    return results
def add_post(filename, post):
    data=read_json(filename)
    data.append(post)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)