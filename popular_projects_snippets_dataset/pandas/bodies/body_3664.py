# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
df = DataFrame({"A": ["a", "b"], "B": ["c", "d"], "C": [1, 2]}).set_index(
    ["A", "B"]
)
result = df.rename(str.upper)
expected = df.rename(index=str.upper)
tm.assert_frame_equal(result, expected)
