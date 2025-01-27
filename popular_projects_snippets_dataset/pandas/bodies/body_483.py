# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
with pytest.raises(ValueError, match="Invalid frequency: xx"):
    PeriodDtype("xx")

for s in ["period[D]", "Period[D]", "D"]:
    dt = PeriodDtype(s)
    assert dt.freq == pd.tseries.offsets.Day()
    assert is_period_dtype(dt)

for s in ["period[3D]", "Period[3D]", "3D"]:
    dt = PeriodDtype(s)
    assert dt.freq == pd.tseries.offsets.Day(3)
    assert is_period_dtype(dt)

for s in [
    "period[26H]",
    "Period[26H]",
    "26H",
    "period[1D2H]",
    "Period[1D2H]",
    "1D2H",
]:
    dt = PeriodDtype(s)
    assert dt.freq == pd.tseries.offsets.Hour(26)
    assert is_period_dtype(dt)
