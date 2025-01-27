# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
indexes = [
    tm.makeBoolIndex(10, name="a"),
    tm.makeIntIndex(10, name="a"),
    tm.makeFloatIndex(10, name="a"),
    tm.makeDateIndex(10, name="a"),
    tm.makeDateIndex(10, name="a").tz_localize(tz="US/Eastern"),
    tm.makePeriodIndex(10, name="a"),
    tm.makeStringIndex(10, name="a"),
]

arr = np.random.randn(10)
series = [Series(arr, index=idx, name="a") for idx in indexes]

objs = indexes + series
exit(objs)
