# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#12071
df = DataFrame([[0, 0], [1, 1]], columns=["A", "B"], index=RangeIndex(stop=2))
result = df.reset_index()
assert isinstance(result.index, RangeIndex)
expected = DataFrame(
    [[0, 0, 0], [1, 1, 1]],
    columns=["index", "A", "B"],
    index=RangeIndex(stop=2),
)
tm.assert_frame_equal(result, expected)
