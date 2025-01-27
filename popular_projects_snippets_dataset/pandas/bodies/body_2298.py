# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# invalid conditions
df = DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
cond = df > 0

err1 = (df + 1).values[0:2, :]
msg = "other must be the same shape as self when an ndarray"
with pytest.raises(ValueError, match=msg):
    df.where(cond, err1)

err2 = cond.iloc[:2, :].values
other1 = _safe_add(df)
msg = "Array conditional must be same shape as self"
with pytest.raises(ValueError, match=msg):
    df.where(err2, other1)

with pytest.raises(ValueError, match=msg):
    df.mask(True)
with pytest.raises(ValueError, match=msg):
    df.mask(0)
