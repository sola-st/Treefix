# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
val = np.int64(val)
td = Timedelta(val)

assert method(td, "ns") == td

res = method(td, "us")
nanos = 1000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0

res = method(td, "ms")
nanos = 1_000_000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0

res = method(td, "s")
nanos = 1_000_000_000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0

res = method(td, "min")
nanos = 60 * 1_000_000_000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0

res = method(td, "h")
nanos = 60 * 60 * 1_000_000_000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0

res = method(td, "D")
nanos = 24 * 60 * 60 * 1_000_000_000
assert np.abs((res - td).value) < nanos
assert res.value % nanos == 0
