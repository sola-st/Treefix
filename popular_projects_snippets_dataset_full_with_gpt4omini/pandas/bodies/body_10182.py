# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# https://github.com/twosigma/pandas/issues/53
typ = np.dtype(any_int_numpy_dtype).type
size = 1000
idx = np.repeat(typ(0), size)
idx[-1] = 1

val = 5e25
arr = np.repeat(val, size)
arr[0] = np.nan
arr[-1] = 0

df = DataFrame(
    {
        "index": idx,
        "adl2": arr,
    }
).set_index("index")
result = df.groupby("index")["adl2"].rolling(window=10, min_periods=1).mean()
expected = Series(
    arr,
    name="adl2",
    index=MultiIndex.from_arrays(
        [
            Index([0] * 999 + [1], dtype=typ, name="index"),
            Index([0] * 999 + [1], dtype=typ, name="index"),
        ],
    ),
)
tm.assert_series_equal(result, expected)
