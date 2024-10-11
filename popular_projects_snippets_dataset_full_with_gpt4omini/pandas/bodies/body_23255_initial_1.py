import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

x = np.array([1, 7, 5, 4, 6, 3]) # pragma: no cover
_preprocess_for_cut = lambda x: x # pragma: no cover
_coerce_to_type = lambda x: (x, x.dtype) # pragma: no cover
bins = 3 # pragma: no cover
is_scalar = lambda x: np.isscalar(x) # pragma: no cover
right = True # pragma: no cover
nanops = type('Mock', (object,), {'nanmin': np.nanmin, 'nanmax': np.nanmax})() # pragma: no cover
IntervalIndex = pd.IntervalIndex # pragma: no cover
is_datetime64tz_dtype = lambda x: False # pragma: no cover
_convert_bin_to_numeric_type = lambda bins, dtype: bins # pragma: no cover
_bins_to_cuts = lambda x, bins, **kwargs: (np.digitize(x, bins), bins) # pragma: no cover
labels = None # pragma: no cover
precision = 3 # pragma: no cover
include_lowest = False # pragma: no cover
duplicates = 'raise' # pragma: no cover
ordered = True # pragma: no cover
_postprocess_for_cut = lambda fac, bins, retbins, dtype, original: fac # pragma: no cover
retbins = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
from l3.Runtime import _l_
"""
    Bin values into discrete intervals.

    Use `cut` when you need to segment and sort data values into bins. This
    function is also useful for going from a continuous variable to a
    categorical variable. For example, `cut` could convert ages to groups of
    age ranges. Supports binning into an equal number of bins, or a
    pre-specified array of bins.

    Parameters
    ----------
    x : array-like
        The input array to be binned. Must be 1-dimensional.
    bins : int, sequence of scalars, or IntervalIndex
        The criteria to bin by.

        * int : Defines the number of equal-width bins in the range of `x`. The
          range of `x` is extended by .1% on each side to include the minimum
          and maximum values of `x`.
        * sequence of scalars : Defines the bin edges allowing for non-uniform
          width. No extension of the range of `x` is done.
        * IntervalIndex : Defines the exact bins to be used. Note that
          IntervalIndex for `bins` must be non-overlapping.

    right : bool, default True
        Indicates whether `bins` includes the rightmost edge or not. If
        ``right == True`` (the default), then the `bins` ``[1, 2, 3, 4]``
        indicate (1,2], (2,3], (3,4]. This argument is ignored when
        `bins` is an IntervalIndex.
    labels : array or False, default None
        Specifies the labels for the returned bins. Must be the same length as
        the resulting bins. If False, returns only integer indicators of the
        bins. This affects the type of the output container (see below).
        This argument is ignored when `bins` is an IntervalIndex. If True,
        raises an error. When `ordered=False`, labels must be provided.
    retbins : bool, default False
        Whether to return the bins or not. Useful when bins is provided
        as a scalar.
    precision : int, default 3
        The precision at which to store and display the bins labels.
    include_lowest : bool, default False
        Whether the first interval should be left-inclusive or not.
    duplicates : {default 'raise', 'drop'}, optional
        If bin edges are not unique, raise ValueError or drop non-uniques.
    ordered : bool, default True
        Whether the labels are ordered or not. Applies to returned types
        Categorical and Series (with Categorical dtype). If True,
        the resulting categorical will be ordered. If False, the resulting
        categorical will be unordered (labels must be provided).

        .. versionadded:: 1.1.0

    Returns
    -------
    out : Categorical, Series, or ndarray
        An array-like object representing the respective bin for each value
        of `x`. The type depends on the value of `labels`.

        * None (default) : returns a Series for Series `x` or a
          Categorical for all other inputs. The values stored within
          are Interval dtype.

        * sequence of scalars : returns a Series for Series `x` or a
          Categorical for all other inputs. The values stored within
          are whatever the type in the sequence is.

        * False : returns an ndarray of integers.

    bins : numpy.ndarray or IntervalIndex.
        The computed or specified bins. Only returned when `retbins=True`.
        For scalar or sequence `bins`, this is an ndarray with the computed
        bins. If set `duplicates=drop`, `bins` will drop non-unique bin. For
        an IntervalIndex `bins`, this is equal to `bins`.

    See Also
    --------
    qcut : Discretize variable into equal-sized buckets based on rank
        or based on sample quantiles.
    Categorical : Array type for storing data that come from a
        fixed set of values.
    Series : One-dimensional array with axis labels (including time series).
    IntervalIndex : Immutable Index implementing an ordered, sliceable set.

    Notes
    -----
    Any NA values will be NA in the result. Out of bounds values will be NA in
    the resulting Series or Categorical object.

    Reference :ref:`the user guide <reshaping.tile.cut>` for more examples.

    Examples
    --------
    Discretize into three equal-sized bins.

    >>> pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
    ... # doctest: +ELLIPSIS
    [(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
    Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...

    >>> pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, retbins=True)
    ... # doctest: +ELLIPSIS
    ([(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
    Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...
    array([0.994, 3.   , 5.   , 7.   ]))

    Discovers the same bins, but assign them specific labels. Notice that
    the returned Categorical's categories are `labels` and is ordered.

    >>> pd.cut(np.array([1, 7, 5, 4, 6, 3]),
    ...        3, labels=["bad", "medium", "good"])
    ['bad', 'good', 'medium', 'medium', 'good', 'bad']
    Categories (3, object): ['bad' < 'medium' < 'good']

    ``ordered=False`` will result in unordered categories when labels are passed.
    This parameter can be used to allow non-unique labels:

    >>> pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3,
    ...        labels=["B", "A", "B"], ordered=False)
    ['B', 'B', 'A', 'A', 'B', 'B']
    Categories (2, object): ['A', 'B']

    ``labels=False`` implies you just want the bins back.

    >>> pd.cut([0, 1, 1, 2], bins=4, labels=False)
    array([0, 1, 1, 3])

    Passing a Series as an input returns a Series with categorical dtype:

    >>> s = pd.Series(np.array([2, 4, 6, 8, 10]),
    ...               index=['a', 'b', 'c', 'd', 'e'])
    >>> pd.cut(s, 3)
    ... # doctest: +ELLIPSIS
    a    (1.992, 4.667]
    b    (1.992, 4.667]
    c    (4.667, 7.333]
    d     (7.333, 10.0]
    e     (7.333, 10.0]
    dtype: category
    Categories (3, interval[float64, right]): [(1.992, 4.667] < (4.667, ...

    Passing a Series as an input returns a Series with mapping value.
    It is used to map numerically to intervals based on bins.

    >>> s = pd.Series(np.array([2, 4, 6, 8, 10]),
    ...               index=['a', 'b', 'c', 'd', 'e'])
    >>> pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False)
    ... # doctest: +ELLIPSIS
    (a    1.0
     b    2.0
     c    3.0
     d    4.0
     e    NaN
     dtype: float64,
     array([ 0,  2,  4,  6,  8, 10]))

    Use `drop` optional when bins is not unique

    >>> pd.cut(s, [0, 2, 4, 6, 10, 10], labels=False, retbins=True,
    ...        right=False, duplicates='drop')
    ... # doctest: +ELLIPSIS
    (a    1.0
     b    2.0
     c    3.0
     d    3.0
     e    NaN
     dtype: float64,
     array([ 0,  2,  4,  6, 10]))

    Passing an IntervalIndex for `bins` results in those categories exactly.
    Notice that values not covered by the IntervalIndex are set to NaN. 0
    is to the left of the first bin (which is closed on the right), and 1.5
    falls between two bins.

    >>> bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])
    >>> pd.cut([0, 0.5, 1.5, 2.5, 4.5], bins)
    [NaN, (0.0, 1.0], NaN, (2.0, 3.0], (4.0, 5.0]]
    Categories (3, interval[int64, right]): [(0, 1] < (2, 3] < (4, 5]]
    """
# NOTE: this binning code is changed a bit from histogram for var(x) == 0

original = x
_l_(10671)
x = _preprocess_for_cut(x)
_l_(10672)
x, dtype = _coerce_to_type(x)
_l_(10673)

if not np.iterable(bins):
    _l_(10705)

    if is_scalar(bins) and bins < 1:
        _l_(10675)

        raise ValueError("`bins` should be a positive integer.")
        _l_(10674)

    try:
        _l_(10680)

        sz = x.size
        _l_(10676)
    except AttributeError:
        _l_(10679)

        x = np.asarray(x)
        _l_(10677)
        sz = x.size
        _l_(10678)

    if sz == 0:
        _l_(10682)

        raise ValueError("Cannot cut empty array")
        _l_(10681)

    rng = (nanops.nanmin(x), nanops.nanmax(x))
    _l_(10683)
    mn, mx = (mi + 0.0 for mi in rng)
    _l_(10684)

    if np.isinf(mn) or np.isinf(mx):
        _l_(10686)

        # GH 24314
        raise ValueError(
            "cannot specify integer `bins` when input data contains infinity"
        )
        _l_(10685)
    if mn == mx:
        _l_(10695)

        mn -= 0.001 * abs(mn) if mn != 0 else 0.001
        _l_(10687)
        mx += 0.001 * abs(mx) if mx != 0 else 0.001
        _l_(10688)
        bins = np.linspace(mn, mx, bins + 1, endpoint=True)
        _l_(10689)
    else:  # adjust end points after binning
        bins = np.linspace(mn, mx, bins + 1, endpoint=True)
        _l_(10690)
        adj = (mx - mn) * 0.001  # 0.1% of the range
        _l_(10691)  # 0.1% of the range
        if right:
            _l_(10694)

            bins[0] -= adj
            _l_(10692)
        else:
            bins[-1] += adj
            _l_(10693)

elif isinstance(bins, IntervalIndex):
    _l_(10704)

    if bins.is_overlapping:
        _l_(10697)

        raise ValueError("Overlapping IntervalIndex is not accepted.")
        _l_(10696)

else:
    if is_datetime64tz_dtype(bins):
        _l_(10700)

        bins = np.asarray(bins, dtype=DT64NS_DTYPE)
        _l_(10698)
    else:
        bins = np.asarray(bins)
        _l_(10699)
    bins = _convert_bin_to_numeric_type(bins, dtype)
    _l_(10701)

    # GH 26045: cast to float64 to avoid an overflow
    if (np.diff(bins.astype("float64")) < 0).any():
        _l_(10703)

        raise ValueError("bins must increase monotonically.")
        _l_(10702)

fac, bins = _bins_to_cuts(
    x,
    bins,
    right=right,
    labels=labels,
    precision=precision,
    include_lowest=include_lowest,
    dtype=dtype,
    duplicates=duplicates,
    ordered=ordered,
)
_l_(10706)
aux = _postprocess_for_cut(fac, bins, retbins, dtype, original)
_l_(10707)

exit(aux)
