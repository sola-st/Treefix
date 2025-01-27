# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 35964 - path within _wrap_applied_output not hit by a test
grouped = df.groupby(["A", "B"], as_index=False)
result = grouped.apply(len)
expected = grouped.count().rename(columns={"C": np.nan}).drop(columns="D")
# TODO(GH#34306): Use assert_frame_equal when column name is not np.nan
tm.assert_index_equal(result.index, expected.index)
tm.assert_numpy_array_equal(result.values, expected.values)
