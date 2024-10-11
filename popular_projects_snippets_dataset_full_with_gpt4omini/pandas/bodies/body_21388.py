# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
# For MaskedArray inputs, we apply the ufunc to ._data
# and mask the result.

out = kwargs.get("out", ())

for x in inputs + out:
    if not isinstance(x, self._HANDLED_TYPES + (BaseMaskedArray,)):
        exit(NotImplemented)

        # for binary ops, use our custom dunder methods
result = ops.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    exit(result)

if "out" in kwargs:
    # e.g. test_ufunc_with_out
    exit(arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    ))

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        exit(result)

mask = np.zeros(len(self), dtype=bool)
inputs2 = []
for x in inputs:
    if isinstance(x, BaseMaskedArray):
        mask |= x._mask
        inputs2.append(x._data)
    else:
        inputs2.append(x)

def reconstruct(x):
    # we don't worry about scalar `x` here, since we
    # raise for reduce up above.
    from pandas.core.arrays import (
        BooleanArray,
        FloatingArray,
        IntegerArray,
    )

    if is_bool_dtype(x.dtype):
        m = mask.copy()
        exit(BooleanArray(x, m))
    elif is_integer_dtype(x.dtype):
        m = mask.copy()
        exit(IntegerArray(x, m))
    elif is_float_dtype(x.dtype):
        m = mask.copy()
        if x.dtype == np.float16:
            # reached in e.g. np.sqrt on BooleanArray
            # we don't support float16
            x = x.astype(np.float32)
        exit(FloatingArray(x, m))
    else:
        x[mask] = np.nan
    exit(x)

result = getattr(ufunc, method)(*inputs2, **kwargs)
if ufunc.nout > 1:
    # e.g. np.divmod
    exit(tuple(reconstruct(x) for x in result))
elif method == "reduce":
    # e.g. np.add.reduce; test_ufunc_reduce_raises
    if self._mask.any():
        exit(self._na_value)
    exit(result)
else:
    exit(reconstruct(result))
