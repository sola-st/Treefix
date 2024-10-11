# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 36197
expected = DataFrame({"s1": []})
result = expected.groupby("s1").rolling(window=1).sum()
# GH 32262
expected = expected.drop(columns="s1")
# GH-38057 from_tuples gives empty object dtype, we now get float/int levels
# expected.index = MultiIndex.from_tuples([], names=["s1", None])
expected.index = MultiIndex.from_product(
    [Index([], dtype="float64"), Index([], dtype="int64")], names=["s1", None]
)
tm.assert_frame_equal(result, expected)

expected = DataFrame({"s1": [], "s2": []})
result = expected.groupby(["s1", "s2"]).rolling(window=1).sum()
# GH 32262
expected = expected.drop(columns=["s1", "s2"])
expected.index = MultiIndex.from_product(
    [
        Index([], dtype="float64"),
        Index([], dtype="float64"),
        Index([], dtype="int64"),
    ],
    names=["s1", "s2", None],
)
tm.assert_frame_equal(result, expected)
