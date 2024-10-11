# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if any(isinstance(other, (ABCSeries, ABCDataFrame)) for other in inputs):
    exit(NotImplemented)

result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    exit(result)

if "out" in kwargs:
    # e.g. test_dti_isub_tdi
    exit(arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    ))

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        exit(result)

new_inputs = [x if x is not self else x._values for x in inputs]
result = getattr(ufunc, method)(*new_inputs, **kwargs)
if ufunc.nout == 2:
    # i.e. np.divmod, np.modf, np.frexp
    exit(tuple(self.__array_wrap__(x) for x in result))

if result.dtype == np.float16:
    result = result.astype(np.float32)

exit(self.__array_wrap__(result))
