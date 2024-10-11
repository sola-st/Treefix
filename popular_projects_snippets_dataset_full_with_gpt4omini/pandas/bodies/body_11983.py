# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """\
KORD,19990127 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000
KORD,19990127 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000
KORD,19990127 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000
KORD,19990127 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000
KORD,19990127 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000
"""
parser = all_parsers
kwds = {
    "header": None,
    "parse_dates": [1],
    "index_col": 1,
    "names": ["X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7"],
}
result = parser.read_csv(StringIO(data), **kwds)

index = Index(
    [
        datetime(1999, 1, 27, 19, 0),
        datetime(1999, 1, 27, 20, 0),
        datetime(1999, 1, 27, 21, 0),
        datetime(1999, 1, 27, 21, 0),
        datetime(1999, 1, 27, 22, 0),
    ],
    name="X1",
)
expected = DataFrame(
    [
        ["KORD", " 18:56:00", 0.81, 2.81, 7.2, 0.0, 280.0],
        ["KORD", " 19:56:00", 0.01, 2.21, 7.2, 0.0, 260.0],
        ["KORD", " 20:56:00", -0.59, 2.21, 5.7, 0.0, 280.0],
        ["KORD", " 21:18:00", -0.99, 2.01, 3.6, 0.0, 270.0],
        ["KORD", " 21:56:00", -0.59, 1.71, 5.1, 0.0, 290.0],
    ],
    columns=["X0", "X2", "X3", "X4", "X5", "X6", "X7"],
    index=index,
)
if parser.engine == "pyarrow" and not pa_version_under6p0:
    # https://github.com/pandas-dev/pandas/issues/44231
    # pyarrow 6.0 starts to infer time type
    expected["X2"] = pd.to_datetime("1970-01-01" + expected["X2"]).dt.time

tm.assert_frame_equal(result, expected)
