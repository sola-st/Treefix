# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dr = date_range(start=Timestamp("2000-02-27"), periods=5, freq="S")
r1 = pd.Index([x.to_julian_date() for x in dr])
r2 = dr.to_julian_date()
assert isinstance(r2, pd.Index) and r2.dtype == np.float64
tm.assert_index_equal(r1, r2)
