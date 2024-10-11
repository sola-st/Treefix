# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# See gh-1693
parser = all_parsers
if parser.engine == "pyarrow" and pa_version_under7p0:
    request.node.add_marker(pytest.mark.xfail(reason="Fails for pyarrow < 7.0"))
data = "Date,x\n2012-06-13T01:39:00Z,0.5"

result = parser.read_csv(StringIO(data), index_col=0, parse_dates=True)
expected = DataFrame(
    {"x": [0.5]}, index=Index([Timestamp("2012-06-13 01:39:00+00:00")], name="Date")
)
tm.assert_frame_equal(result, expected)
if parser.engine == "pyarrow":
    expected_tz = pytz.utc
else:
    expected_tz = timezone.utc
assert result.index.tz is expected_tz
