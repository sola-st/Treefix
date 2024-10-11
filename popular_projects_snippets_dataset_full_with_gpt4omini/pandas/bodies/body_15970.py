# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop.py

ser = Series(data=data, index=index)
result = ser.drop(drop_labels, axis=axis)
expected = Series(data=expected_data, index=expected_index)
tm.assert_series_equal(result, expected)
