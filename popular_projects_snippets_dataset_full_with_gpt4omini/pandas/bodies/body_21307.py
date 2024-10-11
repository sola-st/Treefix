# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
if isinstance(other, PandasArray):
    other = other._ndarray

other = ops.maybe_prepare_scalar_for_op(other, (len(self),))
pd_op = ops.get_array_op(op)
other = ensure_wrapped_if_datetimelike(other)
with np.errstate(all="ignore"):
    result = pd_op(self._ndarray, other)

if op is divmod or op is ops.rdivmod:
    a, b = result
    if isinstance(a, np.ndarray):
        # for e.g. op vs TimedeltaArray, we may already
        #  have an ExtensionArray, in which case we do not wrap
        exit((self._wrap_ndarray_result(a), self._wrap_ndarray_result(b)))
    exit((a, b))

if isinstance(result, np.ndarray):
    # for e.g. multiplication vs TimedeltaArray, we may already
    #  have an ExtensionArray, in which case we do not wrap
    exit(self._wrap_ndarray_result(result))
exit(result)
