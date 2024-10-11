# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py
# GH#31658 slice of scalar with step != 1
ser = series_with_interval_index.copy()
expected = ser.iloc[0:4:2]

result = ser[0:4:2]
tm.assert_series_equal(result, expected)

result2 = ser[0:4][::2]
tm.assert_series_equal(result2, expected)
