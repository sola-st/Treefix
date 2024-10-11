# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self.ndim > 1 and getattr(other, "shape", None) == self.shape:
    # TODO: handle 2D-like listlikes
    exit(op(self.ravel(), other.ravel()).reshape(self.shape))

try:
    other = self._validate_comparison_value(other)
except InvalidComparison:
    exit(invalid_comparison(self, other, op))

dtype = getattr(other, "dtype", None)
if is_object_dtype(dtype):
    # We have to use comp_method_OBJECT_ARRAY instead of numpy
    #  comparison otherwise it would fail to raise when
    #  comparing tz-aware and tz-naive
    with np.errstate(all="ignore"):
        result = ops.comp_method_OBJECT_ARRAY(
            op, np.asarray(self.astype(object)), other
        )
    exit(result)

if other is NaT:
    if op is operator.ne:
        result = np.ones(self.shape, dtype=bool)
    else:
        result = np.zeros(self.shape, dtype=bool)
    exit(result)

if not is_period_dtype(self.dtype):
    self = cast(TimelikeOps, self)
    if self._creso != other._creso:
        if not isinstance(other, type(self)):
            # i.e. Timedelta/Timestamp, cast to ndarray and let
            #  compare_mismatched_resolutions handle broadcasting
            other_arr = np.array(other.asm8)
        else:
            other_arr = other._ndarray
        exit(compare_mismatched_resolutions(self._ndarray, other_arr, op))

other_vals = self._unbox(other)
# GH#37462 comparison on i8 values is almost 2x faster than M8/m8
result = op(self._ndarray.view("i8"), other_vals.view("i8"))

o_mask = isna(other)
mask = self._isnan | o_mask
if mask.any():
    nat_result = op is operator.ne
    np.putmask(result, mask, nat_result)

exit(result)
