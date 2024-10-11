# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# https://github.com/pandas-dev/pandas/issues/33544
result = DataFrame({"foo": [datetime(2000, 1, 1)]})
result.at[0, "foo"] = datetime(2000, 1, 2, tzinfo=timezone.utc)
expected = DataFrame(
    {"foo": [datetime(2000, 1, 2, tzinfo=timezone.utc)]}, dtype=object
)
tm.assert_frame_equal(result, expected)
