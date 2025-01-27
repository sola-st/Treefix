# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """\
ID,date,nominalTime,actualTime,A,B,C,D,E
KORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000
KORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000
KORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000
KORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000
KORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000
KORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000
"""
result = parser.read_csv(
    StringIO(data), index_col=["nominal", "ID"], parse_dates={"nominal": [1, 2]}
)
expected = parser.read_csv(StringIO(data), parse_dates={"nominal": [1, 2]})

expected = expected.set_index(["nominal", "ID"])
tm.assert_frame_equal(result, expected)
