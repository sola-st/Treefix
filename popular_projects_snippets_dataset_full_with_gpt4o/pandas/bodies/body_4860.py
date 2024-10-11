# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
ser = Series(["a_b_c", "c_d_e", np.nan, "f_g_h"])
result = ser.str.split("_").str.get(1)
expected = Series(["b", "d", np.nan, "g"])
tm.assert_series_equal(result, expected)
