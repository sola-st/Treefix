# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH 49024
parser = all_parsers
data = "Date,test\n2012-01-01,1\n,2"
parser.read_csv_check_warnings(
    UserWarning,
    "The argument 'infer_datetime_format' is deprecated",
    StringIO(data),
    parse_dates=["Date"],
    infer_datetime_format=True,
)
