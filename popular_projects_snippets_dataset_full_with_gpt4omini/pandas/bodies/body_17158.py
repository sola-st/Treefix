# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
dti = date_range("2016-01-01", periods=3, tz="Europe/Amsterdam")
df = DataFrame({"A": np.random.randn(3), "B": np.random.randn(3), "C": dti})
result = df.pivot_table(index=["B", "C"], dropna=False)

# check tz retention
assert result.index.levels[1].equals(dti)
