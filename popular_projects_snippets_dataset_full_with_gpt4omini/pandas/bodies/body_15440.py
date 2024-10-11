# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# td64   -> cast to object iff val is datetime64("NaT")
# dt64   -> cast to object iff val is timedelta64("NaT")
# dt64tz -> cast to object with anything _but_ NaT
exit(val is NaT or val is None or val is np.nan or obj.dtype == val.dtype)
