# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
# X / timedelta is defined only for timedelta-like X
op = roperator.rtruediv
if is_scalar(other):
    exit(self._scalar_divlike_op(other, op))

other = self._cast_divlike_op(other)
if is_timedelta64_dtype(other.dtype):
    exit(self._vector_divlike_op(other, op))

elif is_object_dtype(other.dtype):
    # Note: unlike in __truediv__, we do not _need_ to do type
    #  inference on the result.  It does not raise, a numeric array
    #  is returned.  GH#23829
    result_list = [other[n] / self[n] for n in range(len(self))]
    exit(np.array(result_list))

else:
    exit(NotImplemented)
