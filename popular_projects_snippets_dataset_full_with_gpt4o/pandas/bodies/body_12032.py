# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH#13378
parser = all_parsers
data = """A
20150908
20150909
"""
result = parser.read_csv(
    StringIO(data), parse_dates={"date": ["A"]}, keep_date_col=True
)
expected_data = [Timestamp("2015-09-08"), Timestamp("2015-09-09")]
expected = DataFrame({"date": expected_data, "A": expected_data})
tm.assert_frame_equal(result, expected)
