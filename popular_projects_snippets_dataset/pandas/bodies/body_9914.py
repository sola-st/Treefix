# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
df = DataFrame({"A": range(5), "B": range(5, 10), "C": "foo"})
r = df.rolling(window=3, step=step)
with pytest.raises(DataError, match="Cannot aggregate non-numeric type: object"):
    # GH#42738, enforced in 2.0
    r.sum()
