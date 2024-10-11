# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_delete.py
idx = timedelta_range(start="1 days", periods=10, freq="D", name="idx")

# preserve freq
expected_0_2 = timedelta_range(start="4 days", periods=7, freq="D", name="idx")
expected_7_9 = timedelta_range(start="1 days", periods=7, freq="D", name="idx")

# reset freq to None
expected_3_5 = TimedeltaIndex(
    ["1 d", "2 d", "3 d", "7 d", "8 d", "9 d", "10d"], freq=None, name="idx"
)

cases = {
    (0, 1, 2): expected_0_2,
    (7, 8, 9): expected_7_9,
    (3, 4, 5): expected_3_5,
}
for n, expected in cases.items():
    result = idx.delete(n)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq

    result = idx.delete(slice(n[0], n[-1] + 1))
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
