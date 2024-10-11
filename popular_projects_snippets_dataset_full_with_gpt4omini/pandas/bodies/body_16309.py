# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

s = Series(iNaT, dtype="M8[ns]", index=range(5))
assert isna(s).all()

# in theory this should be all nulls, but since
# we are not specifying a dtype is ambiguous
s = Series(iNaT, index=range(5))
assert not isna(s).all()

s = Series(np.nan, dtype="M8[ns]", index=range(5))
assert isna(s).all()

s = Series([datetime(2001, 1, 2, 0, 0), iNaT], dtype="M8[ns]")
assert isna(s[1])
assert s.dtype == "M8[ns]"

s = Series([datetime(2001, 1, 2, 0, 0), np.nan], dtype="M8[ns]")
assert isna(s[1])
assert s.dtype == "M8[ns]"
