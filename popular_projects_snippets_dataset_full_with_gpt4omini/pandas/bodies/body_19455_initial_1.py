import numpy as np # pragma: no cover

data = [[1, 2, 3], [4, 5, 6]] # pragma: no cover
def is_list_like(x): return isinstance(x, (list, np.ndarray)) # pragma: no cover
data = np.array(data) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
from l3.Runtime import _l_
"""
    Check if we should use nested_data_to_arrays.
    """
aux = (
    len(data) > 0
    and is_list_like(data[0])
    and getattr(data[0], "ndim", 1) == 1
    and not (isinstance(data, ExtensionArray) and data.ndim == 2)
)
_l_(10514)
exit(aux)
