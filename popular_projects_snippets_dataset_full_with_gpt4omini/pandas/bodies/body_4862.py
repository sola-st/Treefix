# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
ser = Series(["1_2_3_4_5", "6_7_8_9_10", "11_12"])
result = ser.str.split("_").str.get(idx)
expected = Series(["3", "8", np.nan])
tm.assert_series_equal(result, expected)
