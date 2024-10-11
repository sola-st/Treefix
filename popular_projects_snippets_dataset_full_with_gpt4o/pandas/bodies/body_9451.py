# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
arr = np.arange(8).astype(np.int64).view("m8[s]").astype("m8[ns]").reshape(4, 2)
arr[-1, -1] = "Nat"

tda = TimedeltaArray(arr)

result = tda.sum(skipna=False)
assert result is pd.NaT

result = tda.sum(axis=0, skipna=False)
expected = pd.TimedeltaIndex([Timedelta(seconds=12), pd.NaT])._values
tm.assert_timedelta_array_equal(result, expected)

result = tda.sum(axis=1, skipna=False)
expected = pd.TimedeltaIndex(
    [
        Timedelta(seconds=1),
        Timedelta(seconds=5),
        Timedelta(seconds=9),
        pd.NaT,
    ]
)._values
tm.assert_timedelta_array_equal(result, expected)
