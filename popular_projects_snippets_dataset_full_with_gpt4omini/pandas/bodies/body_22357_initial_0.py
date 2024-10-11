import numpy as np # pragma: no cover
class HashTable: pass # pragma: no cover

def _ensure_data(values): return np.array(values) # pragma: no cover
values = ['apple', 'banana', 'cherry'] # pragma: no cover
def _check_object_for_strings(arr): return arr.dtype if arr.dtype == np.object else 'other' # pragma: no cover
_hashtables = {'object': HashTable()} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
from l3.Runtime import _l_
"""
    Parameters
    ----------
    values : np.ndarray

    Returns
    -------
    htable : HashTable subclass
    values : ndarray
    """
values = _ensure_data(values)
_l_(4763)

ndtype = _check_object_for_strings(values)
_l_(4764)
hashtable = _hashtables[ndtype]
_l_(4765)
aux = (hashtable, values)
_l_(4766)
exit(aux)
