import numpy as np # pragma: no cover

_ensure_data = lambda x: x if isinstance(x, np.ndarray) else np.array(x) # pragma: no cover
values = np.array(['a', 'b', 'c'], dtype=object) # pragma: no cover
_check_object_for_strings = lambda x: 'object' if x.dtype == object else 'other' # pragma: no cover
_hashtables = {'object': type('MockHashTable', (object,), {})()} # pragma: no cover

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
_l_(16001)

ndtype = _check_object_for_strings(values)
_l_(16002)
hashtable = _hashtables[ndtype]
_l_(16003)
aux = (hashtable, values)
_l_(16004)
exit(aux)
