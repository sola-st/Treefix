# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#25775, testing that sorting by index works with a multi-index.
df = DataFrame(
    {"a": [3, 1, 2], "b": [0, 0, 0], "c": [0, 1, 2], "d": list("abc")}
)
result = df.set_index(list("abc")).sort_index(level=list("ba"))

expected = DataFrame(
    {"a": [1, 2, 3], "b": [0, 0, 0], "c": [1, 2, 0], "d": list("bca")}
)
expected = expected.set_index(list("abc"))

tm.assert_frame_equal(result, expected)
