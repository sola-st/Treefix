dr = 2 # pragma: no cover
y = 3 # pragma: no cover
x = 4 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
from l3.Runtime import _l_
aux = [dr * y, dr * x]
_l_(9898)
exit(aux)
