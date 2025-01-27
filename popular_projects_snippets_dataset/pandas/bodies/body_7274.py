# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
# GH#19147
tdi = TimedeltaIndex(["1 days 01:00:00", "2 days 01:00:00"], freq=None)
with pytest.raises(NullFrequencyError, match="Cannot shift with no freq"):
    tdi.shift(2)
