# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
pydates = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3)]
dates = [np.datetime64(x) for x in pydates]

dts = Series(dates, dtype="datetime64[ns]")

# valid astype
dts.astype("int64")

# invalid casting
msg = r"Converting from datetime64\[ns\] to int32 is not supported"
with pytest.raises(TypeError, match=msg):
    dts.astype("int32")

# ints are ok
# we test with np.int64 to get similar results on
# windows / 32-bit platforms
result = Series(dts, dtype=np.int64)
expected = Series(dts.astype(np.int64))
tm.assert_series_equal(result, expected)
