# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
df = Series(["a", "b", "c"])
with pytest.raises(TypeError, match="no numeric data to plot"):
    df.plot()
