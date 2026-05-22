import json
with open("tasks.json", 'r') as f:
    data = json.load(f)
    

for task in data:
    print(task['status'].upper())