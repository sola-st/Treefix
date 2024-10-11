# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py

td = Series([timedelta(days=i) for i in range(10)])

# nan ops on timedeltas
td1 = td.copy()
td1[0] = np.nan
assert isna(td1[0])
assert td1[0].value == iNaT
td1[0] = td[0]
assert not isna(td1[0])

# GH#16674 iNaT is treated as an integer when given by the user
td1[1] = iNaT
assert not isna(td1[1])
assert td1.dtype == np.object_
assert td1[1] == iNaT
td1[1] = td[1]
assert not isna(td1[1])

td1[2] = NaT
assert isna(td1[2])
assert td1[2].value == iNaT
td1[2] = td[2]
assert not isna(td1[2])

# boolean setting
# GH#2899 boolean setting
td3 = np.timedelta64(timedelta(days=3))
td7 = np.timedelta64(timedelta(days=7))
td[(td > td3) & (td < td7)] = np.nan
assert isna(td).sum() == 3
