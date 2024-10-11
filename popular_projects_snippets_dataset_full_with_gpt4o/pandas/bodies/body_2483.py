# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#45779
df = DataFrame(
    data=[[0], [1]],
    index=MultiIndex.from_tuples([("a",), ("b",)], names=["first"]),
)
expected = DataFrame(
    data=[[0]], index=MultiIndex.from_tuples([("a",)], names=["first"])
)
result = df.loc["a"]
tm.assert_frame_equal(result, expected)
