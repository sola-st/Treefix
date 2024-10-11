# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH 14313
ser = empty_series_dti
result = ser.resample(freq, group_keys=False).apply(lambda x: 1)
expected = ser.resample(freq).apply(np.sum)

tm.assert_series_equal(result, expected, check_dtype=False)
