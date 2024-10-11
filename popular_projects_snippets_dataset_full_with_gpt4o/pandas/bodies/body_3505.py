# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
# #15593 #15617
# test 1
df1 = DataFrame({"A": [1.0, 2, 3], "B": date_range("2000", periods=3)})
df2 = DataFrame({"A": [None, 2, 3]})
expected = df1.copy()
df1.update(df2, overwrite=False)

tm.assert_frame_equal(df1, expected)

# test 2
df1 = DataFrame({"A": [1.0, None, 3], "B": date_range("2000", periods=3)})
df2 = DataFrame({"A": [None, 2, 3]})
expected = DataFrame({"A": [1.0, 2, 3], "B": date_range("2000", periods=3)})
df1.update(df2, overwrite=False)

tm.assert_frame_equal(df1, expected)
