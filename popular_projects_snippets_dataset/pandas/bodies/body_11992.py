# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """date,A,B,C
20090101,a,1,2
20090102,b,3,4
20090103,c,4,5
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col="date", parse_dates=["date"])
# freq doesn't round-trip
index = DatetimeIndex(
    list(date_range("1/1/2009", periods=3)), name="date", freq=None
)

expected = DataFrame(
    {"A": ["a", "b", "c"], "B": [1, 3, 4], "C": [2, 4, 5]}, index=index
)
tm.assert_frame_equal(result, expected)
