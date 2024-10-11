import numpy as np # pragma: no cover

values = np.array([1, 2, 3, 4, 5]) # pragma: no cover
mask = np.array([False, True, False, True, False]) # pragma: no cover
qs = np.array([25, 50, 75], dtype=np.float64) # pragma: no cover
na_value = np.nan # pragma: no cover
np_percentile_argname = 'interpolation' # pragma: no cover
interpolation = 'linear' # pragma: no cover
np.full = lambda size, fill_value: np.array([fill_value] * size) # pragma: no cover
np.percentile = lambda values, qs, **kwargs: np.array([np.percentile(values, q, **kwargs) for q in qs]) # pragma: no cover

import numpy as np # pragma: no cover

values = np.array([1.0, 2.0, 3.0, 4.0, np.nan]) # pragma: no cover
mask = np.array([False, False, False, False, True]) # pragma: no cover
qs = np.array([25.0, 50.0, 75.0], dtype=np.float64) # pragma: no cover
na_value = np.nan # pragma: no cover
np_percentile_argname = 'interpolation' # pragma: no cover
interpolation = 'linear' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/array_algos/quantile.py
from l3.Runtime import _l_
"""
    Wrapper for np.percentile that skips missing values, specialized to
    1-dimensional case.

    Parameters
    ----------
    values : array over which to find quantiles
    mask : ndarray[bool]
        locations in values that should be considered missing
    qs : np.ndarray[float64] of quantile indices to find
    na_value : scalar
        value to return for empty or all-null values
    interpolation : str

    Returns
    -------
    quantiles : scalar or array
    """
# mask is Union[ExtensionArray, ndarray]
values = values[~mask]
_l_(16603)

if len(values) == 0:
    _l_(16605)

    aux = np.full(len(qs), na_value)
    _l_(16604)
    # Can't pass dtype=values.dtype here bc we might have na_value=np.nan
    #  with values.dtype=int64 see test_quantile_empty
    # equiv: 'np.array([na_value] * len(qs))' but much faster
    exit(aux)
aux = np.percentile(
    values,
    qs,
    # error: No overload variant of "percentile" matches argument
    # types "ndarray[Any, Any]", "ndarray[Any, dtype[floating[_64Bit]]]"
    # , "Dict[str, str]"  [call-overload]
    **{np_percentile_argname: interpolation},  # type: ignore[call-overload]
)
_l_(16606)

exit(aux)
