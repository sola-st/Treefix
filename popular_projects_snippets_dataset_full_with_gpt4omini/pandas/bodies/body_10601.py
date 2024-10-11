# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH28426
gr = Series([1, 2, 3]).groupby([0, 0, 1])
grouped = gr.agg(a="sum", b="sum")
expected = DataFrame({"a": [3, 3], "b": [3, 3]}, index=np.array([0, 1]))
tm.assert_frame_equal(expected, grouped)
