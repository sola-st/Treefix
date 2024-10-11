# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#17235
if using_array_manager:
    mark = pytest.mark.xfail(
        reason="Incorrect type inference on NaT in reduction result"
    )
    request.node.add_marker(mark)

arr = np.arange(8).astype(np.int64).view("m8[s]").reshape(4, 2)
arr[-1, -1] = "Nat"

df = DataFrame(arr)
assert (df.dtypes == arr.dtype).all()

result = df.sum(skipna=False)
expected = Series([pd.Timedelta(seconds=12), pd.NaT], dtype="m8[s]")
tm.assert_series_equal(result, expected)

result = df.sum(axis=0, skipna=False)
tm.assert_series_equal(result, expected)

result = df.sum(axis=1, skipna=False)
expected = Series(
    [
        pd.Timedelta(seconds=1),
        pd.Timedelta(seconds=5),
        pd.Timedelta(seconds=9),
        pd.NaT,
    ],
    dtype="m8[s]",
)
tm.assert_series_equal(result, expected)
