# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
arr = TimedeltaArray._from_sequence([Timedelta("1H"), Timedelta("2H")])

if np.dtype(dtype) != np.int64:
    with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
        arr.astype(dtype)
    exit()

result = arr.astype(dtype)
expected = arr._ndarray.view("i8")
tm.assert_numpy_array_equal(result, expected)
