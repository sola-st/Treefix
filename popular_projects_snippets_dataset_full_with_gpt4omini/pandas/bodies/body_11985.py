# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """05/31/2012,15:30:00.029,1306.25,1,E,0,,1306.25
05/31/2012,15:30:00.029,1306.25,8,E,0,,1306.25"""

result = parser.read_csv(
    StringIO(data), parse_dates=[[0, 1]], header=None, date_parser=Timestamp
)
expected = DataFrame(
    [
        [
            Timestamp("05/31/2012, 15:30:00.029"),
            1306.25,
            1,
            "E",
            0,
            np.nan,
            1306.25,
        ],
        [
            Timestamp("05/31/2012, 15:30:00.029"),
            1306.25,
            8,
            "E",
            0,
            np.nan,
            1306.25,
        ],
    ],
    columns=["0_1", 2, 3, 4, 5, 6, 7],
)
tm.assert_frame_equal(result, expected)
