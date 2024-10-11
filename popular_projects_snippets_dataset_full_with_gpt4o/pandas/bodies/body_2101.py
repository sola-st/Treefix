# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# mixed tzs will raise if errors='raise'
# https://github.com/pandas-dev/pandas/issues/50585
arr = [
    Timestamp("2013-01-01 13:00:00", tz="US/Pacific"),
    Timestamp("2013-01-02 14:00:00", tz="US/Eastern"),
]
msg = (
    "Tz-aware datetime.datetime cannot be "
    "converted to datetime64 unless utc=True"
)
with pytest.raises(ValueError, match=msg):
    to_datetime(arr, cache=cache)

result = to_datetime(arr, cache=cache, errors="ignore")
expected = Index(
    [
        Timestamp("2013-01-01 13:00:00-08:00"),
        Timestamp("2013-01-02 14:00:00-05:00"),
    ],
    dtype="object",
)
tm.assert_index_equal(result, expected)
result = to_datetime(arr, cache=cache, errors="coerce")
expected = DatetimeIndex(
    ["2013-01-01 13:00:00-08:00", "NaT"], dtype="datetime64[ns, US/Pacific]"
)
tm.assert_index_equal(result, expected)
