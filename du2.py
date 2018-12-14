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


with open ('input.geojson', encoding='utf-8') as f:
    json_map = json.loads(f.read())
features = json_map['features']
# print(features)


i = 1
for feature in features:
    feature['properties']['cluster'] = i
    i += 1


bbox = list(calc_bbox(features))
print(bbox)


# print(json.dumps(json_map, ensure_ascii=False, indent=2))
with open('output.geojson', 'a') as outfile:
    json.dump(json_map, outfile)
