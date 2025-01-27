# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# https://github.com/pandas-dev/pandas/issues/21390

df = DataFrame(
    {
        "key1": Categorical(list("abcbabcba")),
        "key2": Categorical(
            list(pd.date_range("2018-06-01 00", freq="1T", periods=3)) * 3
        ),
        "values": np.arange(9),
    }
)
result = df.groupby(["key1", "key2"]).mean()

idx = MultiIndex.from_product(
    [
        Categorical(["a", "b", "c"]),
        Categorical(pd.date_range("2018-06-01 00", freq="1T", periods=3)),
    ],
    names=["key1", "key2"],
)
expected = DataFrame({"values": [0, 4, 8, 3, 4, 5, 6, np.nan, 2]}, index=idx)
tm.assert_frame_equal(result, expected)
