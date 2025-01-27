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
