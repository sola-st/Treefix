# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
result = parser.read_csv(StringIO(data), date_parser=pd.to_datetime, **kwargs)

# Python can sometimes be flaky about how
# the aggregated columns are entered, so
# this standardizes the order.
result = result[expected.columns]
tm.assert_frame_equal(result, expected)
