import json

with open("./json/raw_data/issues.json") as f:
    data = json.load(f)

for issue in data:
    if "ts" not in issue["files_exts"] and "js" not in issue["files_exts"] and "py" not in issue["files_exts"]:
        data.remove(issue)

with open("./json/raw_data/issues.json", "w") as f:
    json.dump(data, f, indent=4)