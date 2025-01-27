# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH-19810
df = DataFrame({"A": [1, 2]})

with pytest.raises(ImportError, match="matplotlib is required for plotting"):
    df.plot()
