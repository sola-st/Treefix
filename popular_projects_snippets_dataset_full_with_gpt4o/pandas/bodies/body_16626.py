# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# see gh-13936
dtype = np.dtype(any_real_numpy_dtype).type

df1 = pd.DataFrame(
    {
        "value": [5, 2, 25, 100, 78, 120, 79],
        "key": [1, 2, 3, 2, 3, 1, 2],
        "symbol": list("ABCDEFG"),
    },
    columns=["symbol", "key", "value"],
)
df1.value = dtype(df1.value)

df2 = pd.DataFrame(
    {"value": [0, 80, 120, 125], "key": [1, 2, 2, 3], "result": list("xyzw")},
    columns=["value", "key", "result"],
)
df2.value = dtype(df2.value)

df1 = df1.sort_values("value").reset_index(drop=True)
result = merge_asof(df1, df2, on="value", by="key")

expected = pd.DataFrame(
    {
        "symbol": list("BACEGDF"),
        "key": [2, 1, 3, 3, 2, 2, 1],
        "value": [2, 5, 25, 78, 79, 100, 120],
        "result": [np.nan, "x", np.nan, np.nan, np.nan, "y", "x"],
    },
    columns=["symbol", "key", "value", "result"],
)
expected.value = dtype(expected.value)

tm.assert_frame_equal(result, expected)
