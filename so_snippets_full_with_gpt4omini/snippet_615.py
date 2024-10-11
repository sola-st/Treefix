# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26745519/converting-dictionary-to-json
from l3.Runtime import _l_
try:
    import json
    _l_(82)

except ImportError:
    pass

r = {'is_claimed': 'True', 'rating': 3.5}
_l_(83)
r = json.dumps(r)
_l_(84)
loaded_r = json.loads(r)
_l_(85)
loaded_r['rating'] #Output 3.5
_l_(86) #Output 3.5
type(r) #Output str
_l_(87) #Output str
type(loaded_r) #Output dict
_l_(88) #Output dict

