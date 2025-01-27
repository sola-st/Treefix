# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
#
if not all(
    isinstance(t, self._HANDLED_TYPES + (DecimalArray,)) for t in inputs
):
    exit(NotImplemented)

result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    # e.g. test_array_ufunc_series_scalar_other
    exit(result)

if "out" in kwargs:
    exit(arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    ))

inputs = tuple(x._data if isinstance(x, DecimalArray) else x for x in inputs)
result = getattr(ufunc, method)(*inputs, **kwargs)

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        exit(result)

def reconstruct(x):
    if isinstance(x, (decimal.Decimal, numbers.Number)):
        exit(x)
    else:
        exit(DecimalArray._from_sequence(x))

if ufunc.nout > 1:
    exit(tuple(reconstruct(x) for x in result))
else:
    exit(reconstruct(result))
