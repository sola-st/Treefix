# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
from l3.Runtime import _l_
def lowercase_keys(obj):
  _l_(1496)

  if isinstance(obj, dict):
    _l_(1494)

    obj = {key.lower(): value for key, value in obj.items()}
    _l_(1488)
    for key, value in obj.items():
      _l_(1493)

      if isinstance(value, list):
        _l_(1491)

        for idx, item in enumerate(value):
          _l_(1490)

          value[idx] = lowercase_keys(item)
          _l_(1489)
      obj[key] = lowercase_keys(value)
      _l_(1492)
  aux = obj 
  _l_(1495) 
  return aux 

json_str = {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}], "EMB_DICT": {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}]}}
_l_(1497)

lowercase_keys(json_str)
_l_(1498)


Out[0]: {'foo': 'BAR',
 'bar': 123,
 'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}],
 'emb_dict': {'foo': 'BAR',
  'bar': 123,
  'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}]}}
_l_(1499)

