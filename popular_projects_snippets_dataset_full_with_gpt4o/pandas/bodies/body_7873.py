# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
# GH#13149, GH#13209
idx = PeriodIndex(["2016-05-16", "NaT", NaT, np.NaN], freq="D")
msg = "Cannot cast PeriodIndex to dtype"
with pytest.raises(TypeError, match=msg):
    idx.astype(dtype)
