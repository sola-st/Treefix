# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
test1 = DataFrame(
    np.zeros((6, 3)),
    index=date_range(
        "2012-11-15 00:00:00", periods=6, freq="100L", tz="US/Central"
    ),
)
test2 = DataFrame(
    np.zeros((3, 3)),
    index=date_range(
        "2012-11-15 00:00:00", periods=3, freq="250L", tz="US/Central"
    ),
    columns=range(3, 6),
)

result = test1.join(test2, how="outer")
expected = test1.index.union(test2.index)

tm.assert_index_equal(result.index, expected)
assert result.index.tz.zone == "US/Central"
