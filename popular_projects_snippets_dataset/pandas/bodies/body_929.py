# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py

# as timestamp is not a tuple!
dates = date_range("1/1/2000", periods=8)
df = DataFrame(np.random.randn(8, 4), index=dates, columns=["A", "B", "C", "D"])
s = df["A"]

result = s.at[dates[5]]
xp = s.values[5]
assert result == xp
