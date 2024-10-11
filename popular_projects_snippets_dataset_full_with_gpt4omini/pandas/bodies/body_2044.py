# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
actual = to_timedelta(val)
assert actual.value == np.timedelta64("NaT").astype("int64")
