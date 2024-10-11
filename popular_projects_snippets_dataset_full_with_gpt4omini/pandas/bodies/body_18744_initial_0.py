import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

index = range(5) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/conftest.py
from l3.Runtime import _l_
"""Helper for the _series dict"""
size = len(index)
_l_(9726)
data = np.random.randn(size)
_l_(9727)
aux = Series(data, index=index, name="a")
_l_(9728)
exit(aux)
