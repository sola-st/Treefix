# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Create an array.

    Parameters
    ----------
    data : Sequence of objects
        The scalars inside `data` should be instances of the
        scalar type for `dtype`. It's expected that `data`
        represents a 1-dimensional array of data.

        When `data` is an Index or Series, the underlying array
        will be extracted from `data`.

    dtype : str, np.dtype, or ExtensionDtype, optional
        The dtype to use for the array. This may be a NumPy
        dtype or an extension type registered with pandas using
        :meth:`pandas.api.extensions.register_extension_dtype`.

        If not specified, there are two possibilities:

        1. When `data` is a :class:`Series`, :class:`Index`, or
           :class:`ExtensionArray`, the `dtype` will be taken
           from the data.
        2. Otherwise, pandas will attempt to infer the `dtype`
           from the data.

        Note that when `data` is a NumPy array, ``data.dtype`` is
        *not* used for inferring the array type. This is because
        NumPy cannot represent all the types of data that can be
        held in extension arrays.

        Currently, pandas will infer an extension dtype for sequences of

        ============================== =======================================
        Scalar Type                    Array Type
        ============================== =======================================
        :class:`pandas.Interval`       :class:`pandas.arrays.IntervalArray`
        :class:`pandas.Period`         :class:`pandas.arrays.PeriodArray`
        :class:`datetime.datetime`     :class:`pandas.arrays.DatetimeArray`
        :class:`datetime.timedelta`    :class:`pandas.arrays.TimedeltaArray`
        :class:`int`                   :class:`pandas.arrays.IntegerArray`
        :class:`float`                 :class:`pandas.arrays.FloatingArray`
        :class:`str`                   :class:`pandas.arrays.StringArray` or
                                       :class:`pandas.arrays.ArrowStringArray`
        :class:`bool`                  :class:`pandas.arrays.BooleanArray`
        ============================== =======================================

        The ExtensionArray created when the scalar type is :class:`str` is determined by
        ``pd.options.mode.string_storage`` if the dtype is not explicitly given.

        For all other cases, NumPy's usual inference rules will be used.

        .. versionchanged:: 1.0.0

           Pandas infers nullable-integer dtype for integer data,
           string dtype for string data, and nullable-boolean dtype
           for boolean data.

        .. versionchanged:: 1.2.0

            Pandas now also infers nullable-floating dtype for float-like
            input data

    copy : bool, default True
        Whether to copy the data, even if not necessary. Depending
        on the type of `data`, creating the new array may require
        copying data, even if ``copy=False``.

    Returns
    -------
    ExtensionArray
        The newly created array.

    Raises
    ------
    ValueError
        When `data` is not 1-dimensional.

    See Also
    --------
    numpy.array : Construct a NumPy array.
    Series : Construct a pandas Series.
    Index : Construct a pandas Index.
    arrays.PandasArray : ExtensionArray wrapping a NumPy array.
    Series.array : Extract the array stored within a Series.

    Notes
    -----
    Omitting the `dtype` argument means pandas will attempt to infer the
    best array type from the values in the data. As new array types are
    added by pandas and 3rd party libraries, the "best" array type may
    change. We recommend specifying `dtype` to ensure that

    1. the correct array type for the data is returned
    2. the returned array type doesn't change as new extension types
       are added by pandas and third-party libraries

    Additionally, if the underlying memory representation of the returned
    array matters, we recommend specifying the `dtype` as a concrete object
    rather than a string alias or allowing it to be inferred. For example,
    a future version of pandas or a 3rd-party library may include a
    dedicated ExtensionArray for string data. In this event, the following
    would no longer return a :class:`arrays.PandasArray` backed by a NumPy
    array.

    >>> pd.array(['a', 'b'], dtype=str)
    <PandasArray>
    ['a', 'b']
    Length: 2, dtype: str32

    This would instead return the new ExtensionArray dedicated for string
    data. If you really need the new array to be backed by a  NumPy array,
    specify that in the dtype.

    >>> pd.array(['a', 'b'], dtype=np.dtype("<U1"))
    <PandasArray>
    ['a', 'b']
    Length: 2, dtype: str32

    Finally, Pandas has arrays that mostly overlap with NumPy

      * :class:`arrays.DatetimeArray`
      * :class:`arrays.TimedeltaArray`

    When data with a ``datetime64[ns]`` or ``timedelta64[ns]`` dtype is
    passed, pandas will always return a ``DatetimeArray`` or ``TimedeltaArray``
    rather than a ``PandasArray``. This is for symmetry with the case of
    timezone-aware data, which NumPy does not natively support.

    >>> pd.array(['2015', '2016'], dtype='datetime64[ns]')
    <DatetimeArray>
    ['2015-01-01 00:00:00', '2016-01-01 00:00:00']
    Length: 2, dtype: datetime64[ns]

    >>> pd.array(["1H", "2H"], dtype='timedelta64[ns]')
    <TimedeltaArray>
    ['0 days 01:00:00', '0 days 02:00:00']
    Length: 2, dtype: timedelta64[ns]

    Examples
    --------
    If a dtype is not specified, pandas will infer the best dtype from the values.
    See the description of `dtype` for the types pandas infers for.

    >>> pd.array([1, 2])
    <IntegerArray>
    [1, 2]
    Length: 2, dtype: Int64

    >>> pd.array([1, 2, np.nan])
    <IntegerArray>
    [1, 2, <NA>]
    Length: 3, dtype: Int64

    >>> pd.array([1.1, 2.2])
    <FloatingArray>
    [1.1, 2.2]
    Length: 2, dtype: Float64

    >>> pd.array(["a", None, "c"])
    <StringArray>
    ['a', <NA>, 'c']
    Length: 3, dtype: string

    >>> with pd.option_context("string_storage", "pyarrow"):
    ...     arr = pd.array(["a", None, "c"])
    ...
    >>> arr
    <ArrowStringArray>
    ['a', <NA>, 'c']
    Length: 3, dtype: string

    >>> pd.array([pd.Period('2000', freq="D"), pd.Period("2000", freq="D")])
    <PeriodArray>
    ['2000-01-01', '2000-01-01']
    Length: 2, dtype: period[D]

    You can use the string alias for `dtype`

    >>> pd.array(['a', 'b', 'a'], dtype='category')
    ['a', 'b', 'a']
    Categories (2, object): ['a', 'b']

    Or specify the actual dtype

    >>> pd.array(['a', 'b', 'a'],
    ...          dtype=pd.CategoricalDtype(['a', 'b', 'c'], ordered=True))
    ['a', 'b', 'a']
    Categories (3, object): ['a' < 'b' < 'c']

    If pandas does not infer a dedicated extension type a
    :class:`arrays.PandasArray` is returned.

    >>> pd.array([1 + 1j, 3 + 2j])
    <PandasArray>
    [(1+1j), (3+2j)]
    Length: 2, dtype: complex128

    As mentioned in the "Notes" section, new extension types may be added
    in the future (by pandas or 3rd party libraries), causing the return
    value to no longer be a :class:`arrays.PandasArray`. Specify the `dtype`
    as a NumPy dtype if you need to ensure there's no future change in
    behavior.

    >>> pd.array([1, 2], dtype=np.dtype("int32"))
    <PandasArray>
    [1, 2]
    Length: 2, dtype: int32

    `data` must be 1-dimensional. A ValueError is raised when the input
    has the wrong dimensionality.

    >>> pd.array(1)
    Traceback (most recent call last):
      ...
    ValueError: Cannot pass scalar '1' to 'pandas.array'.
    """
from pandas.core.arrays import (
    BooleanArray,
    DatetimeArray,
    ExtensionArray,
    FloatingArray,
    IntegerArray,
    IntervalArray,
    PandasArray,
    PeriodArray,
    TimedeltaArray,
)
from pandas.core.arrays.string_ import StringDtype

if lib.is_scalar(data):
    msg = f"Cannot pass scalar '{data}' to 'pandas.array'."
    raise ValueError(msg)

if dtype is None and isinstance(data, (ABCSeries, ABCIndex, ExtensionArray)):
    # Note: we exclude np.ndarray here, will do type inference on it
    dtype = data.dtype

data = extract_array(data, extract_numpy=True)

# this returns None for not-found dtypes.
if isinstance(dtype, str):
    dtype = registry.find(dtype) or dtype

if isinstance(data, ExtensionArray) and (
    dtype is None or is_dtype_equal(dtype, data.dtype)
):
    # e.g. TimedeltaArray[s], avoid casting to PandasArray
    if copy:
        exit(data.copy())
    exit(data)

if is_extension_array_dtype(dtype):
    cls = cast(ExtensionDtype, dtype).construct_array_type()
    exit(cls._from_sequence(data, dtype=dtype, copy=copy))

if dtype is None:
    inferred_dtype = lib.infer_dtype(data, skipna=True)
    if inferred_dtype == "period":
        period_data = cast(Union[Sequence[Optional[Period]], AnyArrayLike], data)
        exit(PeriodArray._from_sequence(period_data, copy=copy))

    elif inferred_dtype == "interval":
        exit(IntervalArray(data, copy=copy))

    elif inferred_dtype.startswith("datetime"):
        # datetime, datetime64
        try:
            exit(DatetimeArray._from_sequence(data, copy=copy))
        except ValueError:
            # Mixture of timezones, fall back to PandasArray
            pass

    elif inferred_dtype.startswith("timedelta"):
        # timedelta, timedelta64
        exit(TimedeltaArray._from_sequence(data, copy=copy))

    elif inferred_dtype == "string":
        # StringArray/ArrowStringArray depending on pd.options.mode.string_storage
        exit(StringDtype().construct_array_type()._from_sequence(data, copy=copy))

    elif inferred_dtype == "integer":
        exit(IntegerArray._from_sequence(data, copy=copy))

    elif (
        inferred_dtype in ("floating", "mixed-integer-float")
        and getattr(data, "dtype", None) != np.float16
    ):
        # GH#44715 Exclude np.float16 bc FloatingArray does not support it;
        #  we will fall back to PandasArray.
        exit(FloatingArray._from_sequence(data, copy=copy))

    elif inferred_dtype == "boolean":
        exit(BooleanArray._from_sequence(data, copy=copy))

    # Pandas overrides NumPy for
    #   1. datetime64[ns]
    #   2. timedelta64[ns]
    # so that a DatetimeArray is returned.
if is_datetime64_ns_dtype(dtype):
    exit(DatetimeArray._from_sequence(data, dtype=dtype, copy=copy))
elif is_timedelta64_ns_dtype(dtype):
    exit(TimedeltaArray._from_sequence(data, dtype=dtype, copy=copy))

exit(PandasArray._from_sequence(data, dtype=dtype, copy=copy))
