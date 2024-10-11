# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
from l3.Runtime import _l_
try:
    import json
    _l_(2187)

except ImportError:
    pass
data = [1,2,3,4,5]
_l_(2188)
with open('no.txt', 'w') as txtfile:
    _l_(2190)

    json.dump(data, txtfile)
    _l_(2189)

