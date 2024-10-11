# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
snap = datetime.today()
n = 50

rng = date_range(snap, periods=n, normalize=False, freq="2D")

offset = timedelta(2)
values = DatetimeIndex([snap + i * offset for i in range(n)], freq=offset)

tm.assert_index_equal(rng, values)

rng = date_range("1/1/2000 08:15", periods=n, normalize=False, freq="B")
the_time = time(8, 15)
for val in rng:
    assert val.time() == the_time
