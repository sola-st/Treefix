# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#45860
df = DataFrame(
    {"a": [1, 2, 2, pd.NA], "b": 100}, dtype=any_numeric_ea_dtype
).set_index(idx)
result = df.drop(Index([2, pd.NA]), level=level)
expected = DataFrame(
    {"a": [1], "b": 100}, dtype=any_numeric_ea_dtype
).set_index(idx)
tm.assert_frame_equal(result, expected)
