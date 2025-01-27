# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 43386
df = DataFrame({"a": ["x", "y", "x"], "b": [0, 1, 2]})
results = list(df.groupby("a").rolling(2))
expecteds = [df.iloc[idx, [1]] for idx in [[0], [0, 2], [1]]]
for result, expected in zip(results, expecteds):
    tm.assert_frame_equal(result, expected)
