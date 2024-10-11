# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_resolution.py
arr = np.array([1], dtype=np.int64)
res = get_resolution(arr, None, NpyDatetimeUnit.NPY_FR_us.value)
assert res == Resolution.RESO_US

res = get_resolution(arr, pytz.UTC, NpyDatetimeUnit.NPY_FR_us.value)
assert res == Resolution.RESO_US
