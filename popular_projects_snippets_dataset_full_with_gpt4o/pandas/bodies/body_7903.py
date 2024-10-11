# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_freq_attr.py
# GH#20678
idx = period_range("2018Q1", periods=4, freq="Q")

# no warning for getter
with tm.assert_produces_warning(None):
    idx.freq

# warning for setter
msg = (
    "property 'freq' of 'PeriodArray' object has no setter"
    if PY311
    else "can't set attribute"
)
with pytest.raises(AttributeError, match=msg):
    idx.freq = offsets.Day()
