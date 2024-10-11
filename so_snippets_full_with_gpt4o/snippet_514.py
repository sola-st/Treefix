# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6130374/empty-set-literal
from l3.Runtime import _l_
s = {*()}  # or {*{}} or {*[]}
_l_(14356)  # or {*{}} or {*[]}
print(s)
_l_(14357)
set()
_l_(14358)

