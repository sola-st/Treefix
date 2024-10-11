# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dti = pd.date_range("2016-01-01", periods=3)

dta = dti._data

fv = dta[-1].tz_localize("UTC")
for invalid in [fv, fv.to_pydatetime()]:
    with pytest.raises(TypeError, match="Cannot compare"):
        dta.shift(1, fill_value=invalid)

dta = dta.tz_localize("UTC")
fv = dta[-1].tz_localize(None)
for invalid in [fv, fv.to_pydatetime(), fv.to_datetime64()]:
    with pytest.raises(TypeError, match="Cannot compare"):
        dta.shift(1, fill_value=invalid)
