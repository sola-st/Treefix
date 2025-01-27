# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#10696, GH#18593
s_data = list("abcaacbab")
s_dtype = CategoricalDtype(list("bac"), ordered=series_ordered)
ser = Series(s_data, dtype=s_dtype, name=name)

# unspecified categories
dtype = CategoricalDtype(ordered=dtype_ordered)
result = ser.astype(dtype)
exp_dtype = CategoricalDtype(s_dtype.categories, dtype_ordered)
expected = Series(s_data, name=name, dtype=exp_dtype)
tm.assert_series_equal(result, expected)

# different categories
dtype = CategoricalDtype(list("adc"), dtype_ordered)
result = ser.astype(dtype)
expected = Series(s_data, name=name, dtype=dtype)
tm.assert_series_equal(result, expected)

if dtype_ordered is False:
    # not specifying ordered, so only test once
    expected = ser
    result = ser.astype("category")
    tm.assert_series_equal(result, expected)
