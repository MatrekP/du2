# Domácí úkol 2 - dělení adresních bodů

Marek Popp
2019-06-27
Praha

## Popis programu
Neinteraktivní program du2.py metodou quadtree dělí adresní body do skupin tak, že žádná skupina nemá více než 50 jednotek.
Adresní body načte ze vstupního souboru input.geojson, přiřadí k nim pořadí a číslo příslušné skupiny a vytvoří výstupní soubor output.geojson.
Program read_output.py tiskne adresní body z výstupního souboru pro jeho čtení

Algoritmus programu du2.py importuje knihovnu json a následně načte vstupní soubor input.geojson a do proměnné features uloží seznam adresních bodů.
Dále přiřadí každému adresnímu bodu pořadí (sequence), spočítá bounding box a spusti funkci quadtree, která rozdělí adresní body do příslušných skupin (cluster_id). 
Nakonec program exportuje výstupní output.geojson.


### Vstup
Soubor input.geojson.


### Výstup
Soubor output.geojson s přiřazeným pořadím (sequence) a skupinou (cluster_id) každému adresnímu bodu.


### Příklad výstupu programu
```
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4882242181",
        "addr:city": "Plzeň",
        "addr:conscriptionnumber": "2861",
        "addr:country": "CZ",
        "addr:housenumber": "2861/2",
        "addr:place": "Jižní Předměstí",
        "addr:postcode": "30100",
        "addr:street": "Radčická",
        "addr:streetnumber": "2",
        "addr:suburb": "Plzeň 3",
        "amenity": "pharmacy",
        "description": "-1. patro, u eskalátorů, po pravé straně",
        "level": "0",
        "name": "Dr.Max",
        "opening_hours": "Mo-Su 09:00-21:00",
        "phone": "+420 377 227 651",
        "ref:ruian:addr": "27289001",
        "source:addr": "cuzk:ruian",
        "website": "https://www.drmax.cz/",
        "sequence": 84,
        "cluster_id": 4
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          13.3693353,
          49.7498031
        ]
      },
      "id": "node/4882242181"
    }
```
