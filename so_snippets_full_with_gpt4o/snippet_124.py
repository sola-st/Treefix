# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2835559/why-cant-python-parse-this-json-data
from l3.Runtime import _l_
{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": [{
        "id": "valore"
    }],
    "om_points": "value",
    "parameters": [{
        "id": "valore"
    }]
}
_l_(14421)
try:
    import json
    _l_(14423)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(14425)

except ImportError:
    pass
with open('data.json') as data_file:
    _l_(14427)

    data_item = json.load(data_file)
    _l_(14426)
pprint(data_item)
_l_(14428)

{'maps': [{'id': 'blabla', 'iscategorical': '0'},
          {'id': 'blabla', 'iscategorical': '0'}],
 'masks': [{'id': 'valore'}],
 'om_points': 'value',
 'parameters': [{'id': 'valore'}]}
_l_(14429)

valore
_l_(14430)

