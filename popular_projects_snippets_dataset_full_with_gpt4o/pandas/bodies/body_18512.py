# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_fields.py
dtindex = np.arange(5, dtype=np.int64) * 10**9 * 3600 * 24 * 32
dtindex.flags.writeable = False
exit(dtindex)
