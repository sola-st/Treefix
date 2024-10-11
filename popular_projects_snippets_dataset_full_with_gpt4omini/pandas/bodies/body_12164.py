# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
# see gh-9079
parser = all_parsers
data = "\n".join(
    [
        "SMOSMANIA ThetaProbe-ML2X ",
        "2007/01/01 01:00   0.2140 U M ",
        "2007/01/01 02:00   0.2141 M O ",
        "2007/01/01 04:00   0.2142 D M ",
    ]
)
expected = DataFrame(
    [
        ["2007/01/01", "01:00", 0.2140, "U", "M"],
        ["2007/01/01", "02:00", 0.2141, "M", "O"],
        ["2007/01/01", "04:00", 0.2142, "D", "M"],
    ],
    columns=["date", "time", "var", "flag", "oflag"],
)

if parser.engine == "python" and lineterminator == "\r":
    mark = pytest.mark.xfail(reason="'CR' not respect with the Python parser yet")
    request.node.add_marker(mark)

data = data.replace("\n", lineterminator)
result = parser.read_csv(
    StringIO(data),
    skiprows=1,
    delim_whitespace=True,
    names=["date", "time", "var", "flag", "oflag"],
)
tm.assert_frame_equal(result, expected)
