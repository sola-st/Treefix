# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_numpy_compat.py
# test ufuncs of numpy, see:
# https://numpy.org/doc/stable/reference/ufuncs.html

if isinstance(index, DatetimeIndexOpsMixin):
    with tm.external_error_raised((TypeError, AttributeError)):
        with np.errstate(all="ignore"):
            func(index)
elif (
    isinstance(index, NumericIndex)
    or (not isinstance(index.dtype, np.dtype) and index.dtype._is_numeric)
    or (index.dtype.kind == "c" and func not in [np.deg2rad, np.rad2deg])
    or index.dtype == bool
):
    # coerces to float (e.g. np.sin)
    with np.errstate(all="ignore"):
        result = func(index)
        arr_result = func(index.values)
        if arr_result.dtype == np.float16:
            arr_result = arr_result.astype(np.float32)
        exp = Index(arr_result, name=index.name)

    tm.assert_index_equal(result, exp)
    if type(index) is not Index or index.dtype == bool:
        assert type(result) is NumericIndex
        if is_complex_dtype(index):
            assert result.dtype == "complex64"
        elif index.dtype in ["bool", "int8", "uint8"]:
            assert result.dtype in ["float16", "float32"]
        elif index.dtype in ["int16", "uint16", "float32"]:
            assert result.dtype == "float32"
        else:
            assert result.dtype == "float64"
    else:
        # e.g. np.exp with Int64 -> Float64
        assert type(result) is Index
else:
    # raise AttributeError or TypeError
    if len(index) == 0:
        pass
    else:
        with tm.external_error_raised((TypeError, AttributeError)):
            with np.errstate(all="ignore"):
                func(index)
