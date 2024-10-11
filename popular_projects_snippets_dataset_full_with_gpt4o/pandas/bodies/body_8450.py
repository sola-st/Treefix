# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#49106 matching reso is OK
dti = date_range("2016-01-01", "2016-01-01 00:00:01", freq="ms", unit="ms")
rng = np.arange(1_451_606_400_000, 1_451_606_401_001, dtype=np.int64)
expected = DatetimeIndex(rng.view("M8[ms]"), freq="ms")
tm.assert_index_equal(dti, expected)

dti = date_range("2016-01-01", "2016-01-01 00:00:01", freq="us", unit="us")
rng = np.arange(1_451_606_400_000_000, 1_451_606_401_000_001, dtype=np.int64)
expected = DatetimeIndex(rng.view("M8[us]"), freq="us")
tm.assert_index_equal(dti, expected)

dti = date_range("2016-01-01", "2016-01-01 00:00:00.001", freq="ns", unit="ns")
rng = np.arange(
    1_451_606_400_000_000_000, 1_451_606_400_001_000_001, dtype=np.int64
)
expected = DatetimeIndex(rng.view("M8[ns]"), freq="ns")
tm.assert_index_equal(dti, expected)
