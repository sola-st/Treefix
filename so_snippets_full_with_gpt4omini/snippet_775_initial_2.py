import json # pragma: no cover

your_json_data = {'key': 'value'} # pragma: no cover
json = type('Mock', (object,), {'dumps': lambda obj, default: '{"key": "value"}', 'loads': lambda obj: {'key': 'value'}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript
from l3.Runtime import _l_
r = json.dumps(your_json_data, default=str)
_l_(1996)
your_json_data = json.loads(r)
_l_(1997)

