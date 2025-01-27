# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# isna_old should work for dt64tz, td64, and period, not just tznaive
dti = date_range("2016-01-01", periods=3)
dta = dti._data
dta[-1] = NaT
expected = np.array([False, False, True], dtype=bool)

objs = [dta, dta.tz_localize("US/Eastern"), dta - dta, dta.to_period("D")]

for obj in objs:
    with cf.option_context("mode.use_inf_as_na", True):
        result = isna(obj)

    tm.assert_numpy_array_equal(result, expected)
