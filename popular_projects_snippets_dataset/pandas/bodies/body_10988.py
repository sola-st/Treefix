# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
grouped = df.groupby(["A", "B"])
result = grouped.apply(len)
expected = grouped.count()["C"]
tm.assert_index_equal(result.index, expected.index)
tm.assert_numpy_array_equal(result.values, expected.values)
