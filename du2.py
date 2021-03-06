import json


def calculate_bbox(features):
    '''
    Spocita bounding box pro adresni body
    :param features: vstupni data features geojsonu
    :return: minx, miny, maxx, maxy
    '''
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


def quadtree(features, cluster):
    '''
    Metoda quadtree, pokud je bodu 50 a mene
    :param features: adresni body
    :param cluster: cislo skupiny
    '''
    if len(features) <= 50:
        # print("<= 50")
        for feature in features:
            feature['properties']['cluster_id'] = cluster
    else:
        quadtree_repeat(features, cluster)


def quadtree_repeat(features, cluster):
    '''
    Metoda quadtree, pokud je bodu vice nez 50
    :param features: adresni body
    :param cluster: cislo skupiny
    '''
    # print("> 50")
    middle = [(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2]
    features1 = []
    features2 = []
    features3 = []
    features4 = []
    for feature in features:
        coordinates = feature['geometry']['coordinates']
        if coordinates[0] > middle[0] and coordinates[1] > middle[1]:
            # feature['properties']['cluster_id'] = cluster + 1
            features1.append(feature)
        if coordinates[0] <= middle[0] and coordinates[1] > middle[1]:
            # feature['properties']['cluster_id'] = cluster + 2
            features2.append(feature)
        if coordinates[0] <= middle[0] and coordinates[1] <= middle[1]:
            # feature['properties']['cluster_id'] = cluster + 3
            features3.append(feature)
        if coordinates[0] > middle[0] and coordinates[1] <= middle[1]:
            # feature['properties']['cluster_id'] = cluster + 4
            features4.append(feature)
    quadtree(features1, cluster + 0)
    quadtree(features2, cluster + 1)
    quadtree(features3, cluster + 2)
    quadtree(features4, cluster + 3)
    # print(features1)


# nacte vstupni geojson
with open ('input.geojson', 'r', encoding='utf-8') as f:
    json_map = json.loads(f.read())
features = json_map['features']
# print(features)


# priradi kazdemu adresnimu bodu poradi
i = 1
for feature in features:
    feature['properties']['sequence'] = i
    i += 1


# spocita bounding box
bbox = list(calculate_bbox(features))
print(bbox)


# spusti rozdelovani adresnich bodu do skupin metodou quadtree
print(len(features))
cluster = 1
quadtree(features, cluster)


# exportuje vystupni geojson
# print(json.dumps(json_map, ensure_ascii=False, indent=2))
with open('output.geojson', 'w') as outfile:
    json.dump(json_map, outfile)
