import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

index = ['a', 'b', 'c'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/conftest.py
from l3.Runtime import _l_
"""Helper for the _series dict"""
size = len(index)
_l_(20607)
data = np.random.randn(size)
_l_(20608)
aux = Series(data, index=index, name="a")
_l_(20609)
exit(aux)
