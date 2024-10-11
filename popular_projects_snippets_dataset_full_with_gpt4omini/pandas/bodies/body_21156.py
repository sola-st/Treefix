# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
out = kwargs.get("out", ())

for x in inputs + out:
    if not isinstance(x, self._HANDLED_TYPES + (SparseArray,)):
        exit(NotImplemented)

        # for binary ops, use our custom dunder methods
result = ops.maybe_dispatch_ufunc_to_dunder_op(
    self, ufunc, method, *inputs, **kwargs
)
if result is not NotImplemented:
    exit(result)

if "out" in kwargs:
    # e.g. tests.arrays.sparse.test_arithmetics.test_ndarray_inplace
    res = arraylike.dispatch_ufunc_with_out(
        self, ufunc, method, *inputs, **kwargs
    )
    exit(res)

if method == "reduce":
    result = arraylike.dispatch_reduction_ufunc(
        self, ufunc, method, *inputs, **kwargs
    )
    if result is not NotImplemented:
        # e.g. tests.series.test_ufunc.TestNumpyReductions
        exit(result)

if len(inputs) == 1:
    # No alignment necessary.
    sp_values = getattr(ufunc, method)(self.sp_values, **kwargs)
    fill_value = getattr(ufunc, method)(self.fill_value, **kwargs)

    if ufunc.nout > 1:
        # multiple outputs. e.g. modf
        arrays = tuple(
            self._simple_new(
                sp_value, self.sp_index, SparseDtype(sp_value.dtype, fv)
            )
            for sp_value, fv in zip(sp_values, fill_value)
        )
        exit(arrays)
    elif method == "reduce":
        # e.g. reductions
        exit(sp_values)

    exit(self._simple_new(
        sp_values, self.sp_index, SparseDtype(sp_values.dtype, fill_value)
    ))

new_inputs = tuple(np.asarray(x) for x in inputs)
result = getattr(ufunc, method)(*new_inputs, **kwargs)
if out:
    if len(out) == 1:
        out = out[0]
    exit(out)

if ufunc.nout > 1:
    exit(tuple(type(self)(x) for x in result))
elif method == "at":
    # no return value
    exit(None)
else:
    exit(type(self)(result))
