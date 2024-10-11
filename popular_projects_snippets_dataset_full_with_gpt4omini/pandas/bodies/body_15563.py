# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH 8306
idx = date_range("20131101", tz="America/Chicago", periods=7)
newidx = date_range("20131103", periods=10, freq="H")
s = Series(range(7), index=idx)
msg = (
    r"Cannot compare dtypes datetime64\[ns, America/Chicago\] "
    r"and datetime64\[ns\]"
)
with pytest.raises(TypeError, match=msg):
    s.reindex(newidx, method="ffill")
