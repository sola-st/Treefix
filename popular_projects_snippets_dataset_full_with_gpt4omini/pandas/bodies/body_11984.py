# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = (
    "KORD,19990127, 19:00:00, 18:56:00, 0.8100\n"
    "KORD,19990127, 20:00:00, 19:56:00, 0.0100\n"
    "KORD,19990127, 21:00:00, 20:56:00, -0.5900\n"
    "KORD,19990127, 21:00:00, 21:18:00, -0.9900\n"
    "KORD,19990127, 22:00:00, 21:56:00, -0.5900\n"
    "KORD,19990127, 23:00:00, 22:56:00, -0.5900"
)
parse_dates = {"actual": [1, 2], "nominal": [1, 3]}
parser = all_parsers

kwds = {
    "header": None,
    "parse_dates": parse_dates,
    "date_parser": pd.to_datetime,
}
result = parser.read_csv(StringIO(data), **kwds)

expected = DataFrame(
    [
        [datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 18, 56), "KORD", 0.81],
        [datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 19, 56), "KORD", 0.01],
        [
            datetime(1999, 1, 27, 21, 0),
            datetime(1999, 1, 27, 20, 56),
            "KORD",
            -0.59,
        ],
        [
            datetime(1999, 1, 27, 21, 0),
            datetime(1999, 1, 27, 21, 18),
            "KORD",
            -0.99,
        ],
        [
            datetime(1999, 1, 27, 22, 0),
            datetime(1999, 1, 27, 21, 56),
            "KORD",
            -0.59,
        ],
        [
            datetime(1999, 1, 27, 23, 0),
            datetime(1999, 1, 27, 22, 56),
            "KORD",
            -0.59,
        ],
    ],
    columns=["actual", "nominal", 0, 4],
)

# Python can sometimes be flaky about how
# the aggregated columns are entered, so
# this standardizes the order.
result = result[expected.columns]
tm.assert_frame_equal(result, expected)
