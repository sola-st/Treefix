# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
self.index = index
self.i8values = index.asi8

# For get_unit_from_dtype we need the dtype to the underlying ndarray,
#  which for tz-aware is not the same as index.dtype
if isinstance(index, ABCIndex):
    # error: Item "ndarray[Any, Any]" of "Union[ExtensionArray,
    # ndarray[Any, Any]]" has no attribute "_ndarray"
    self._creso = get_unit_from_dtype(
        index._data._ndarray.dtype  # type: ignore[union-attr]
    )
else:
    # otherwise we have DTA/TDA
    self._creso = get_unit_from_dtype(index._ndarray.dtype)

# This moves the values, which are implicitly in UTC, to the
# the timezone so they are in local time
if hasattr(index, "tz"):
    if index.tz is not None:
        self.i8values = tz_convert_from_utc(
            self.i8values, index.tz, reso=self._creso
        )

if len(index) < 3:
    raise ValueError("Need at least 3 dates to infer frequency")

self.is_monotonic = (
    self.index._is_monotonic_increasing or self.index._is_monotonic_decreasing
)
