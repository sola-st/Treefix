# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# https://github.com/pandas-dev/pandas/issues/27190
s = Series([], name="name", dtype="float64")
gr = s.groupby([])

result = gr.mean()
expected = s.set_axis(Index([], dtype=np.intp))
tm.assert_series_equal(result, expected)

# check group properties
assert len(gr.grouper.groupings) == 1
tm.assert_numpy_array_equal(
    gr.grouper.group_info[0], np.array([], dtype=np.dtype(np.intp))
)

tm.assert_numpy_array_equal(
    gr.grouper.group_info[1], np.array([], dtype=np.dtype(np.intp))
)

assert gr.grouper.group_info[2] == 0

# check name
assert s.groupby(s).grouper.names == ["name"]
