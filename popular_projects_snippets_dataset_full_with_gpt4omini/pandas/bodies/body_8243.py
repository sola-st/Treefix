# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# GH#19147
dti = DatetimeIndex(["2011-01-01 10:00", "2011-01-01"], freq=None)
with pytest.raises(NullFrequencyError, match="Cannot shift with no freq"):
    dti.shift(2)
