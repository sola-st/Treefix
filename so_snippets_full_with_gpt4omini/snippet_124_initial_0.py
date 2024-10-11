import json # pragma: no cover
from pprint import pprint # pragma: no cover

valore = 'sample_value' # pragma: no cover

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
_l_(2191)
try:
    import json
    _l_(2193)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(2195)

except ImportError:
    pass
with open('data.json') as data_file:
    _l_(2197)

    data_item = json.load(data_file)
    _l_(2196)
pprint(data_item)
_l_(2198)

{'maps': [{'id': 'blabla', 'iscategorical': '0'},
          {'id': 'blabla', 'iscategorical': '0'}],
 'masks': [{'id': 'valore'}],
 'om_points': 'value',
 'parameters': [{'id': 'valore'}]}
_l_(2199)

valore
_l_(2200)

