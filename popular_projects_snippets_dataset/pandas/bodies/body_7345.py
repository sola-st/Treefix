# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tdi = timedelta_range("1 Day", periods=10)
if monotonic == "decreasing":
    tdi = tdi[::-1]
elif monotonic is None:
    taker = np.arange(10, dtype=np.intp)
    np.random.shuffle(taker)
    tdi = tdi.take(taker)
exit(tdi)
