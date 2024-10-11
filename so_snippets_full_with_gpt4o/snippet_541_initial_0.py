Out = {0: None} # pragma: no cover
'foo' # pragma: no cover
'BAR' # pragma: no cover
'bar' # pragma: no cover
'emb_list' # pragma: no cover
'emb_dict' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
from l3.Runtime import _l_
def lowercase_keys(obj):
  _l_(13804)

  if isinstance(obj, dict):
    _l_(13802)

    obj = {key.lower(): value for key, value in obj.items()}
    _l_(13796)
    for key, value in obj.items():
      _l_(13801)

      if isinstance(value, list):
        _l_(13799)

        for idx, item in enumerate(value):
          _l_(13798)

          value[idx] = lowercase_keys(item)
          _l_(13797)
      obj[key] = lowercase_keys(value)
      _l_(13800)
  aux = obj 
  _l_(13803) 
  return aux 

json_str = {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}], "EMB_DICT": {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}]}}
_l_(13805)

lowercase_keys(json_str)
_l_(13806)


Out[0]: {'foo': 'BAR',
 'bar': 123,
 'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}],
 'emb_dict': {'foo': 'BAR',
  'bar': 123,
  'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}]}}
_l_(13807)

