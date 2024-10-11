# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
# Lightly modified version of
# https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
# The primary modification is not boxing scalar return values
# in PandasArray, since pandas' ExtensionArrays are 1-d.
out = kwargs.get("out", ())

result = ops.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    exit(result)

if "out" in kwargs:
    # e.g. test_ufunc_unary
    exit(arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    ))

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        # e.g. tests.series.test_ufunc.TestNumpyReductions
        exit(result)

        # Defer to the implementation of the ufunc on unwrapped values.
inputs = tuple(x._ndarray if isinstance(x, PandasArray) else x for x in inputs)
if out:
    kwargs["out"] = tuple(
        x._ndarray if isinstance(x, PandasArray) else x for x in out
    )
result = getattr(ufunc, method)(*inputs, **kwargs)

if ufunc.nout > 1:
    # multiple return values; re-box array-like results
    exit(tuple(type(self)(x) for x in result))
elif method == "at":
    # no return value
    exit(None)
elif method == "reduce":
    if isinstance(result, np.ndarray):
        # e.g. test_np_reduce_2d
        exit(type(self)(result))

    # e.g. test_np_max_nested_tuples
    exit(result)
else:
    # one return value; re-box array-like results
    exit(type(self)(result))
