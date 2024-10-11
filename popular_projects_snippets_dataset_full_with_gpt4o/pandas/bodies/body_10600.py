# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
gr = Series([1, 2]).groupby([0, 1])
with pytest.raises(TypeError, match="Must provide"):
    gr.agg()

# but we do allow this
result = gr.agg([])
expected = DataFrame(columns=[])
tm.assert_frame_equal(result, expected)
