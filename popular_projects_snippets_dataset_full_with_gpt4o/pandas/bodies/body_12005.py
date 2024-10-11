# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# if we have an invalid date make sure that we handle this with
# and w/o the cache properly.
parser = all_parsers
s = StringIO((f"{value},\n") * 50000)

if parser.engine == "pyarrow":
    # pyarrow reads "0" as 0 (of type int64), and so
    # pandas doesn't try to guess the datetime format
    # TODO: parse dates directly in pyarrow, see
    # https://github.com/pandas-dev/pandas/issues/48017
    warn = None
else:
    warn = UserWarning
parser.read_csv_check_warnings(
    warn,
    "Could not infer format",
    s,
    header=None,
    names=["foo", "bar"],
    parse_dates=["foo"],
    cache_dates=cache_dates,
)
