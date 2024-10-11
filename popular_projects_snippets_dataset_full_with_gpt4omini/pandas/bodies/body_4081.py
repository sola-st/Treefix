# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#30886
df = DataFrame({"A": date_range("2000", periods=4), "B": [1, 2, 3, 4]}).reindex(
    [2, 3, 4]
)
with pytest.raises(TypeError, match="does not support reduction 'sum'"):
    df.sum()
