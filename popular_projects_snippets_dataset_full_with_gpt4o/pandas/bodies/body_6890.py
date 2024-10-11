# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_numpy_compat.py
# test ufuncs of numpy, see:
# https://numpy.org/doc/stable/reference/ufuncs.html
if isinstance(index, (DatetimeIndex, TimedeltaIndex)):

    if func in (np.isfinite, np.isinf, np.isnan):
        # numpy 1.18 changed isinf and isnan to not raise on dt64/td64
        result = func(index)
        assert isinstance(result, np.ndarray)

        out = np.empty(index.shape, dtype=bool)
        func(index, out=out)
        tm.assert_numpy_array_equal(out, result)
    else:
        with tm.external_error_raised(TypeError):
            func(index)

elif isinstance(index, PeriodIndex):
    with tm.external_error_raised(TypeError):
        func(index)

elif (
    isinstance(index, NumericIndex)
    or (not isinstance(index.dtype, np.dtype) and index.dtype._is_numeric)
    or (index.dtype.kind == "c" and func is not np.signbit)
    or index.dtype == bool
):
    # Results in bool array
    result = func(index)
    if not isinstance(index.dtype, np.dtype):
        # e.g. Int64 we expect to get BooleanArray back
        assert isinstance(result, BooleanArray)
    else:
        assert isinstance(result, np.ndarray)

    out = np.empty(index.shape, dtype=bool)
    func(index, out=out)

    if not isinstance(index.dtype, np.dtype):
        tm.assert_numpy_array_equal(out, result._data)
    else:
        tm.assert_numpy_array_equal(out, result)

else:
    if len(index) == 0:
        pass
    else:
        with tm.external_error_raised(TypeError):
            func(index)
