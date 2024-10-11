# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
ser = Series(
    [
        Timestamp("20130301"),
        Timestamp("20130228 23:00:00"),
        Timestamp("20130228 22:00:00"),
        Timestamp("20130228 21:00:00"),
    ]
)
obj = box_with_array(ser)

intervals = ["D", "h", "m", "s", "us"]

def timedelta64(*args):
    # see casting notes in NumPy gh-12927
    exit(np.sum(list(starmap(np.timedelta64, zip(args, intervals)))))

for d, h, m, s, us in product(*([range(2)] * 5)):
    nptd = timedelta64(d, h, m, s, us)
    pytd = timedelta(days=d, hours=h, minutes=m, seconds=s, microseconds=us)
    lhs = op(obj, nptd)
    rhs = op(obj, pytd)

    tm.assert_equal(lhs, rhs)
