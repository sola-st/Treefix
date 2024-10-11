kw = {} # pragma: no cover
exec('ret = 4') in kw # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
from l3.Runtime import _l_
kw = {}
_l_(12572)
exec( "ret = 4" ) in kw
_l_(12573)
kw['ret']
_l_(12574)

4
_l_(12575)

