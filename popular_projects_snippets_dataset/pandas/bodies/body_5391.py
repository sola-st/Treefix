# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
val = np.int64(val)
ts = Timestamp(val)

def checker(res, ts, nanos):
    if method is Timestamp.round:
        diff = np.abs((res - ts).value)
        assert diff <= nanos / 2
    elif method is Timestamp.floor:
        assert res <= ts
    elif method is Timestamp.ceil:
        assert res >= ts

assert method(ts, "ns") == ts

res = method(ts, "us")
nanos = 1000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)

res = method(ts, "ms")
nanos = 1_000_000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)

res = method(ts, "s")
nanos = 1_000_000_000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)

res = method(ts, "min")
nanos = 60 * 1_000_000_000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)

res = method(ts, "h")
nanos = 60 * 60 * 1_000_000_000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)

res = method(ts, "D")
nanos = 24 * 60 * 60 * 1_000_000_000
assert np.abs((res - ts).value) < nanos
assert res.value % nanos == 0
checker(res, ts, nanos)
