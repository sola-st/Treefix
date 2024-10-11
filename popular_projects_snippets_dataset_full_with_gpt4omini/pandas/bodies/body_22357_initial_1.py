import numpy as np # pragma: no cover

def _ensure_data(values): return np.asarray(values) # pragma: no cover
values = np.array(['apple', 'banana', 'cherry']) # pragma: no cover
def _check_object_for_strings(values): return 'str' if np.issubdtype(values.dtype, np.str_) else 'other' # pragma: no cover
_hashtables = {'str': 'StringHashTable', 'other': 'GenericHashTable'} # pragma: no cover

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
