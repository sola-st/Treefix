# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
from l3.Runtime import _l_
for x in list(groupby(range(10))):
    _l_(14235)

    print(list(x[1]))
    _l_(14234)

[]
_l_(14236)
[]
_l_(14237)
[]
_l_(14238)
[]
_l_(14239)
[]
_l_(14240)
[]
_l_(14241)
[]
_l_(14242)
[]
_l_(14243)
[]
_l_(14244)
[9]
_l_(14245)

def groupbylist(*args, **kwargs):
    _l_(14247)

    aux = [(k, list(g)) for k, g in groupby(*args, **kwargs)]
    _l_(14246)
    return aux

