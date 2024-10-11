# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 15853
data = DataFrame({"A": [1, 2], "B": pd.Categorical(["X", "Y"])})
result = melt(data, ["B"], ["A"])
expected = DataFrame(
    {"B": pd.Categorical(["X", "Y"]), "variable": ["A", "A"], "value": [1, 2]}
)

tm.assert_frame_equal(result, expected)
