# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_freq_code.py
ts_np = np.datetime64("2021-01-01T08:00:00.00")
do = to_offset(freqstr)
assert ts_np + do == np.datetime64(expected)
