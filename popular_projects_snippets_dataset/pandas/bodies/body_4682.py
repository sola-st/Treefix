# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
dti = pd.date_range("2016-01-01", periods=3).as_unit(unit)
expected = dti[1]

for obj in [dti, DatetimeArray(dti), Series(dti)]:
    result = nanops.nanmean(obj)
    assert result == expected

dti2 = dti.insert(1, pd.NaT)

for obj in [dti2, DatetimeArray(dti2), Series(dti2)]:
    result = nanops.nanmean(obj)
    assert result == expected
