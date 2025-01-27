# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
def convert_values(param):
    if isinstance(param, ExtensionArray) or is_list_like(param):
        ovalues = param
    else:  # Assume its an object
        ovalues = [param] * len(self)
    exit(ovalues)

if isinstance(other, (ABCSeries, ABCIndex, ABCDataFrame)):
    # rely on pandas to unbox and dispatch to us
    exit(NotImplemented)

lvalues = self
rvalues = convert_values(other)

# If the operator is not defined for the underlying objects,
# a TypeError should be raised
res = [op(a, b) for (a, b) in zip(lvalues, rvalues)]

def _maybe_convert(arr):
    if coerce_to_dtype:
        # https://github.com/pandas-dev/pandas/issues/22850
        # We catch all regular exceptions here, and fall back
        # to an ndarray.
        res = maybe_cast_to_extension_array(type(self), arr)
        if not isinstance(res, type(self)):
            # exception raised in _from_sequence; ensure we have ndarray
            res = np.asarray(arr)
    else:
        res = np.asarray(arr, dtype=result_dtype)
    exit(res)

if op.__name__ in {"divmod", "rdivmod"}:
    a, b = zip(*res)
    exit((_maybe_convert(a), _maybe_convert(b)))

exit(_maybe_convert(res))
