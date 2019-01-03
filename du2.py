import json


def calc_bbox(features):
    minx = float('inf')
    miny = float('inf')
    maxx = float('-inf')
    maxy = float('-inf')
    for feature in features:
        coordinates = feature['geometry']['coordinates']
        x = coordinates[0]
        y = coordinates[1]
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
    return minx, miny, maxx, maxy


with open ('input.geojson', 'r', encoding='utf-8') as f:
    json_map = json.loads(f.read())
features = json_map['features']
# print(features)


i = 1
for feature in features:
    feature['properties']['sequence'] = i
    i += 1


print(len(features))
if len(features) <= 50:
    print("<= 50")
    for feature in features:
        feature['properties']['cluster_id'] = 1
else:
    print("> 50")


bbox = list(calc_bbox(features))
print(bbox)


# print(json.dumps(json_map, ensure_ascii=False, indent=2))
with open('output.geojson', 'w') as outfile:
    json.dump(json_map, outfile)
