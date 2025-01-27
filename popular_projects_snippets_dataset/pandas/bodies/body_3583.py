# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 25775, testing that sorting by index works with a multi-index.
df = DataFrame(
    {"a": ["B", "a", "C"], "b": [0, 1, 0], "c": list("abc"), "d": [0, 1, 2]}
).set_index(list("abc"))

result = df.sort_index(level="a", key=lambda x: x.str.lower())

expected = DataFrame(
    {"a": ["a", "B", "C"], "b": [1, 0, 0], "c": list("bac"), "d": [1, 0, 2]}
).set_index(list("abc"))
tm.assert_frame_equal(result, expected)

result = df.sort_index(
    level=list("abc"),  # can refer to names
    key=lambda x: x.str.lower() if x.name in ["a", "c"] else -x,
)

expected = DataFrame(
    {"a": ["a", "B", "C"], "b": [1, 0, 0], "c": list("bac"), "d": [1, 0, 2]}
).set_index(list("abc"))
tm.assert_frame_equal(result, expected)
