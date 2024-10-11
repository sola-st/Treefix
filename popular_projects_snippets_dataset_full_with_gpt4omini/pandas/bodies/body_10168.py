# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 36889
result = (
    DataFrame({"foo": [2, 1], "bar": [2, 1]})
    .groupby("foo", sort=False)
    .rolling(1)
    .min()
)
expected = DataFrame(
    np.array([[2.0, 2.0], [1.0, 1.0]]),
    columns=["foo", "bar"],
    index=MultiIndex.from_tuples([(2, 0), (1, 1)], names=["foo", None]),
)
# GH 32262
expected = expected.drop(columns="foo")
tm.assert_frame_equal(result, expected)
