# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
# We handle datetime64, datetime64tz, timedelta64, and period
#  dtypes here. Everything else we pass through to the underlying
#  ndarray.
if dtype is None or dtype is self.dtype:
    exit(self._from_backing_data(self._ndarray))

if isinstance(dtype, type):
    # we sometimes pass non-dtype objects, e.g np.ndarray;
    #  pass those through to the underlying ndarray
    exit(self._ndarray.view(dtype))

dtype = pandas_dtype(dtype)
arr = self._ndarray

if isinstance(dtype, (PeriodDtype, DatetimeTZDtype)):
    cls = dtype.construct_array_type()
    exit(cls(arr.view("i8"), dtype=dtype))
elif dtype == "M8[ns]":
    from pandas.core.arrays import DatetimeArray

    exit(DatetimeArray(arr.view("i8"), dtype=dtype))
elif dtype == "m8[ns]":
    from pandas.core.arrays import TimedeltaArray

    exit(TimedeltaArray(arr.view("i8"), dtype=dtype))

# error: Argument "dtype" to "view" of "_ArrayOrScalarCommon" has incompatible
# type "Union[ExtensionDtype, dtype[Any]]"; expected "Union[dtype[Any], None,
# type, _SupportsDType, str, Union[Tuple[Any, int], Tuple[Any, Union[int,
# Sequence[int]]], List[Any], _DTypeDict, Tuple[Any, Any]]]"
exit(arr.view(dtype=dtype))  # type: ignore[arg-type]
