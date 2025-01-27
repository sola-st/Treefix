# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
gr = Series([1, 2, 3]).groupby([0, 0, 1])
result = gr.agg(a=lambda x: 0, b=lambda x: 1)
expected = DataFrame({"a": [0, 0], "b": [1, 1]}, index=np.array([0, 1]))
tm.assert_frame_equal(result, expected)
