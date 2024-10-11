# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
if any(
    isinstance(other, (ABCSeries, ABCIndex, ABCDataFrame)) for other in inputs
):
    exit(NotImplemented)

result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    exit(result)

if "out" in kwargs:
    exit(arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    ))

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        exit(result)

exit(arraylike.default_array_ufunc(self, ufunc, method, *inputs, **kwargs))
