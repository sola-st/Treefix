# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py

tz = tz_aware_fixture
dti = date_range("2016-01-01", periods=3, tz=tz)
dt64vals = dti.values

dtarr = tm.box_expected(dti, box_with_array)
msg = "Cannot subtract tz-naive and tz-aware datetime"
with pytest.raises(TypeError, match=msg):
    dtarr - dt64vals
with pytest.raises(TypeError, match=msg):
    dt64vals - dtarr
