s = 'example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
from l3.Runtime import _l_
"string".upper()
_l_(15227)

s.upper()
_l_(15228)

"string".lower()
_l_(15229)

s.lower()
_l_(15230)

s="sadf"
_l_(15231)
# sadf

s=s.upper()
_l_(15232)
# SADF

