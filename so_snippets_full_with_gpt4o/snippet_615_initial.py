# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26745519/converting-dictionary-to-json
from l3.Runtime import _l_
try:
    import json
    _l_(12297)

except ImportError:
    pass

r = {'is_claimed': 'True', 'rating': 3.5}
_l_(12298)
r = json.dumps(r)
_l_(12299)
loaded_r = json.loads(r)
_l_(12300)
loaded_r['rating'] #Output 3.5
_l_(12301) #Output 3.5
type(r) #Output str
_l_(12302) #Output str
type(loaded_r) #Output dict
_l_(12303) #Output dict

