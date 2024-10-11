from pandas.api.extensions import ExtensionArray # pragma: no cover
from collections.abc import Iterable # pragma: no cover

data = [[1, 2, 3], [4, 5, 6]] # pragma: no cover
def is_list_like(obj): return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)) # pragma: no cover

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
