# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# https://github.com/pandas-dev/pandas/issues/2586
parser = all_parsers
data = """a,b
27.03.2003 14:55:00.000,1
03.08.2003 15:20:00.000,2"""
if parser.engine == "pyarrow":
    expected_index = Index(
        ["27.03.2003 14:55:00.000", "03.08.2003 15:20:00.000"],
        dtype="object",
        name="a",
    )
    warn = None
else:
    expected_index = DatetimeIndex(
        ["2003-03-27 14:55:00", "2003-08-03 15:20:00"],
        dtype="datetime64[ns]",
        name="a",
    )
    warn = UserWarning
msg = r"when dayfirst=False \(the default\) was specified"
result = parser.read_csv_check_warnings(
    warn, msg, StringIO(data), parse_dates=True, index_col=0
)
expected = DataFrame({"b": [1, 2]}, index=expected_index)
tm.assert_frame_equal(result, expected)
