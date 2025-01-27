# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#42771
idx = MultiIndex.from_product([["a", "b"], ["a", "a"]])
df = DataFrame({"x": range(len(idx))}, index=idx)
result = df.drop(index=[("a", "a")])
expected = DataFrame(
    {"x": [2, 3]}, index=MultiIndex.from_tuples([("b", "a"), ("b", "a")])
)
tm.assert_frame_equal(result, expected)
