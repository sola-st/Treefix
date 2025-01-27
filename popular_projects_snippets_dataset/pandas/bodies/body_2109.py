# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# xref 8260
import psycopg2

# https://www.psycopg.org/docs/news.html#what-s-new-in-psycopg-2-9
request.node.add_marker(
    pytest.mark.xfail(
        Version(psycopg2.__version__.split()[0]) > Version("2.8.7"),
        raises=AttributeError,
        reason="psycopg2.tz is deprecated (and appears dropped) in 2.9",
    )
)

# misc cases
tz1 = psycopg2.tz.FixedOffsetTimezone(offset=-300, name=None)
tz2 = psycopg2.tz.FixedOffsetTimezone(offset=-240, name=None)
arr = np.array(
    [
        datetime(2000, 1, 1, 3, 0, tzinfo=tz1),
        datetime(2000, 6, 1, 3, 0, tzinfo=tz2),
    ],
    dtype=object,
)

result = to_datetime(arr, errors="coerce", utc=True, cache=cache)
expected = DatetimeIndex(
    ["2000-01-01 08:00:00+00:00", "2000-06-01 07:00:00+00:00"],
    dtype="datetime64[ns, UTC]",
    freq=None,
)
tm.assert_index_equal(result, expected)

# dtype coercion
i = DatetimeIndex(
    ["2000-01-01 08:00:00"],
    tz=psycopg2.tz.FixedOffsetTimezone(offset=-300, name=None),
)
assert is_datetime64_ns_dtype(i)

# tz coercion
result = to_datetime(i, errors="coerce", cache=cache)
tm.assert_index_equal(result, i)

result = to_datetime(i, errors="coerce", utc=True, cache=cache)
expected = DatetimeIndex(["2000-01-01 13:00:00"], dtype="datetime64[ns, UTC]")
tm.assert_index_equal(result, expected)
