# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 15442
if any_numpy_dtype in (tm.BYTES_DTYPES + tm.STRING_DTYPES):
    data = [1, 2, 2]
    uniques = [1, 2]
elif is_integer_dtype(any_numpy_dtype):
    data = [1, 2, 2]
    uniques = [1, 2]
elif is_float_dtype(any_numpy_dtype):
    data = [1, 2, 2]
    uniques = [1.0, 2.0]
elif is_complex_dtype(any_numpy_dtype):
    data = [complex(1, 0), complex(2, 0), complex(2, 0)]
    uniques = [complex(1, 0), complex(2, 0)]
elif is_bool_dtype(any_numpy_dtype):
    data = [True, True, False]
    uniques = [True, False]
elif is_object_dtype(any_numpy_dtype):
    data = ["A", "B", "B"]
    uniques = ["A", "B"]
else:
    # datetime64[ns]/M8[ns]/timedelta64[ns]/m8[ns] tested elsewhere
    data = [1, 2, 2]
    uniques = [1, 2]

result = Series(data, dtype=any_numpy_dtype).unique()
expected = np.array(uniques, dtype=any_numpy_dtype)

if any_numpy_dtype in tm.STRING_DTYPES:
    expected = expected.astype(object)

if expected.dtype.kind in ["m", "M"]:
    # We get TimedeltaArray/DatetimeArray
    assert isinstance(result, (DatetimeArray, TimedeltaArray))
    result = np.array(result)
tm.assert_numpy_array_equal(result, expected)
