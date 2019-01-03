import json

with open ('output.geojson', 'r', encoding='utf-8') as f:
    json_map = json.loads(f.read())

print(json.dumps(json_map, ensure_ascii=False, indent=2))
