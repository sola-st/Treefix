# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
ser = pd.Series(data_missing)
expected = ser.isna()
with pd.option_context("mode.use_inf_as_na", True):
    result = ser.isna()
self.assert_series_equal(result, expected)
