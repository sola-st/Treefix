# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
from l3.Runtime import _l_
d = {"name":"interpolator",
     "children":[{'name':key,"size":value} for key,value in sample.items()]}
_l_(2314)
json_string = json.dumps(d)
_l_(2315)

