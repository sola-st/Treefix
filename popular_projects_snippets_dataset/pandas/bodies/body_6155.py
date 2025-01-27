# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# data_missing_for_sorting -> [B, NA, A] with A < B and NA missing.
ser = pd.Series(data_missing_for_sorting)
result = getattr(ser, op_name)(skipna=skipna)
tm.assert_almost_equal(result, expected)
