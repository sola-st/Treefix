# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 16454
df = pd.DataFrame({"x": [0], "y": [0], "z": pd.Categorical([0])})
result = merge_asof(df, df, on="x", by=["y", "z"])
expected = pd.DataFrame({"x": [0], "y": [0], "z": pd.Categorical([0])})
tm.assert_frame_equal(result, expected)
