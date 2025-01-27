# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_resolution.py
# don't return the fallback RESO_DAY
arr = np.array([1], dtype=np.int64)
res = get_resolution(arr)
assert res == Resolution.RESO_NS
