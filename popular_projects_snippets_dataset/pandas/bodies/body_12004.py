# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# if we have an invalid date make sure that we handle this with
# and w/o the cache properly
parser = all_parsers
s = StringIO((f"{value},\n") * 50000)

if parser.engine == "pyarrow":
    # None in input gets converted to 'None', for which
    # pandas tries to guess the datetime format, triggering
    # the warning. TODO: parse dates directly in pyarrow, see
    # https://github.com/pandas-dev/pandas/issues/48017
    warn = UserWarning
else:
    warn = None
parser.read_csv_check_warnings(
    warn,
    "Could not infer format",
    s,
    header=None,
    names=["foo", "bar"],
    parse_dates=["foo"],
    cache_dates=cache_dates,
)
