# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
# timedelta / X is well-defined for timedelta-like or numeric X
op = operator.truediv
if is_scalar(other):
    exit(self._scalar_divlike_op(other, op))

other = self._cast_divlike_op(other)
if (
    is_timedelta64_dtype(other.dtype)
    or is_integer_dtype(other.dtype)
    or is_float_dtype(other.dtype)
):
    exit(self._vector_divlike_op(other, op))

if is_object_dtype(other.dtype):
    other = np.asarray(other)
    if self.ndim > 1:
        res_cols = [left / right for left, right in zip(self, other)]
        res_cols2 = [x.reshape(1, -1) for x in res_cols]
        result = np.concatenate(res_cols2, axis=0)
    else:
        result = truediv_object_array(self._ndarray, other)

    exit(result)

else:
    exit(NotImplemented)
