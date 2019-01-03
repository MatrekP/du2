import json


def calculate_bbox(features):
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


bbox = list(calculate_bbox(features))
print(bbox)


cluster = 1
print(len(features))
if len(features) <= 50:
    print("<= 50")
    for feature in features:
        feature['properties']['cluster_id'] = cluster
    cluster += 1
else:
    print("> 50")
    middle = [(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2]
#     quadrant_1 = [middle[0], middle[1], bbox[2], bbox[3]]
#     quadrant_2 = [bbox[0], middle[1], middle[0], bbox[3]]
#     quadrant_3 = [bbox[0], bbox[1], middle[0], middle[1]]
#     quadrant_4 = [middle[0], bbox[1], bbox[2], middle[1]]
    for feature in features:
        coordinates = feature['geometry']['coordinates']
        if coordinates[0] > middle[0] and coordinates[1] > middle[1]:
            feature['properties']['cluster_id'] = 1
        if coordinates[0] <= middle[0] and coordinates[1] > middle[1]:
            feature['properties']['cluster_id'] = 2
        if coordinates[0] <= middle[0] and coordinates[1] <= middle[1]:
            feature['properties']['cluster_id'] = 3
        if coordinates[0] > middle[0] and coordinates[1] <= middle[1]:
            feature['properties']['cluster_id'] = 4


# print(json.dumps(json_map, ensure_ascii=False, indent=2))
with open('output.geojson', 'w') as outfile:
    json.dump(json_map, outfile)
