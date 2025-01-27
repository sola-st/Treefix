# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
rng = date_range("20090415", "20090519", freq="B")
data = {k: 1 for k in rng}

result = Series(data, index=rng)
assert result.index is rng
