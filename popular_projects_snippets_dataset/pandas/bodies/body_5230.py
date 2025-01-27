# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert Timedelta(timedelta(seconds=1)) == np.timedelta64(1, "s").astype(
    "m8[ns]"
)
assert Timedelta(timedelta(microseconds=1)) == np.timedelta64(1, "us").astype(
    "m8[ns]"
)
assert Timedelta(timedelta(days=1)) == np.timedelta64(1, "D").astype("m8[ns]")
