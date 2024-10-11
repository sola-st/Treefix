# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
# GH 30114
ser = Series(original_list)
expected = Series(sorted_list, index=output_index)
kwargs = {
    "ascending": ascending,
    "ignore_index": ignore_index,
    "inplace": inplace,
}

if inplace:
    result_ser = ser.copy()
    result_ser.sort_index(**kwargs)
else:
    result_ser = ser.sort_index(**kwargs)

tm.assert_series_equal(result_ser, expected)
tm.assert_series_equal(ser, Series(original_list))
