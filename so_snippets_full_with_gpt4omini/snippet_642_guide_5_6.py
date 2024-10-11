kw = {} # pragma: no cover
exec("ret = 4", kw) # pragma: no cover
ret_value = kw['ret'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
from l3.Runtime import _l_
kw = {}
_l_(972)
exec( "ret = 4" ) in kw
_l_(973)
kw['ret']
_l_(974)

4
_l_(975)

