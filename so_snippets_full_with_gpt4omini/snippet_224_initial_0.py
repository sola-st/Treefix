dictionary = {'Name': 'harry'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
from l3.Runtime import _l_
dictionary.get("Name",'harry')
_l_(2872)

