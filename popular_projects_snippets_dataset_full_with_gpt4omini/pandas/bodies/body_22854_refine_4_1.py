import numpy as np # pragma: no cover

values = np.array([1, 2, 3, 4, 5, np.nan]) # pragma: no cover
mask = np.array([False, False, False, False, False, True]) # pragma: no cover
qs = np.array([25, 50, 75]) # pragma: no cover
na_value = -1 # pragma: no cover
np_percentile_argname = 'interpolation' # pragma: no cover
interpolation = 'linear' # pragma: no cover

import numpy as np # pragma: no cover

values = np.array([1, 2, 3, 4, 5]) # pragma: no cover
mask = np.array([False, False, False, False, True]) # pragma: no cover
qs = np.array([25, 50, 75]) # pragma: no cover
na_value = -1 # pragma: no cover
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
_l_(6421)

if len(values) == 0:
    _l_(6423)

    aux = np.full(len(qs), na_value)
    _l_(6422)
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
_l_(6424)

exit(aux)
