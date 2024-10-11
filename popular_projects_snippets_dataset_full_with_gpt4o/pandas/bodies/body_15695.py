# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py
# GH 30114
ser = Series(original_list)
expected = Series(sorted_list, index=output_index)
kwargs = {"ignore_index": ignore_index, "inplace": inplace}

if inplace:
    result_ser = ser.copy()
    result_ser.sort_values(ascending=False, **kwargs)
else:
    result_ser = ser.sort_values(ascending=False, **kwargs)

tm.assert_series_equal(result_ser, expected)
tm.assert_series_equal(ser, Series(original_list))
