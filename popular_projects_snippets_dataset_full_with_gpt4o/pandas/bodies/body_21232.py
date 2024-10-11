# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
op = roperator.rfloordiv
if is_scalar(other):
    exit(self._scalar_divlike_op(other, op))

other = self._cast_divlike_op(other)
if is_timedelta64_dtype(other.dtype):
    exit(self._vector_divlike_op(other, op))

elif is_object_dtype(other.dtype):
    result_list = [other[n] // self[n] for n in range(len(self))]
    result = np.array(result_list)
    exit(result)

else:
    exit(NotImplemented)
