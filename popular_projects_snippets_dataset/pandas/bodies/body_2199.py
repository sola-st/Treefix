# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
idx = ["a", "b", "c", "d", "e"]
series = Series(
    ["1/1/2000", np.nan, "1/3/2000", np.nan, "1/5/2000"], index=idx, name="foo"
)
dseries = Series(
    [
        to_datetime("1/1/2000", cache=cache),
        np.nan,
        to_datetime("1/3/2000", cache=cache),
        np.nan,
        to_datetime("1/5/2000", cache=cache),
    ],
    index=idx,
    name="foo",
)

result = to_datetime(series, cache=cache)
dresult = to_datetime(dseries, cache=cache)

expected = Series(np.empty(5, dtype="M8[ns]"), index=idx)
for i in range(5):
    x = series[i]
    if isna(x):
        expected[i] = NaT
    else:
        expected[i] = to_datetime(x, cache=cache)

tm.assert_series_equal(result, expected, check_names=False)
assert result.name == "foo"

tm.assert_series_equal(dresult, expected, check_names=False)
assert dresult.name == "foo"
