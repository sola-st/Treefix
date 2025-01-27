# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta_range.py
# GH#49824
tdi = timedelta_range("0 Days", periods=10, freq="100000D", unit="s")
exp_arr = (np.arange(10, dtype="i8") * 100_000).view("m8[D]").astype("m8[s]")
tm.assert_numpy_array_equal(tdi.to_numpy(), exp_arr)
