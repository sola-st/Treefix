# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
tdser = Series(["59 Days", "59 Days", "NaT"], dtype="timedelta64[ns]")
result = tdser.astype(object)
assert isinstance(result.iloc[0], timedelta)
assert result.dtype == np.object_
