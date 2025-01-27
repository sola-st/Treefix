# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
index = ["A", "B"]
columns = "C"
table = pivot_table(data, index=index, columns=columns)
expected = data.groupby(index + [columns]).agg(np.mean).unstack()
tm.assert_frame_equal(table, expected)
