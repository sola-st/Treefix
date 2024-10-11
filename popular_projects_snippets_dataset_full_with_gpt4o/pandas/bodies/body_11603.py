# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
# see gh-23761.
dialect_name, dialect_kwargs = custom_dialect
parser = all_parsers

expected = DataFrame({"a": [1], "b": [2]})
data = "a:b\n1:2"

warning_klass = None
kwds = {}

# arg=None tests when we pass in the dialect without any other arguments.
if arg is not None:
    if value == "dialect":  # No conflict --> no warning.
        kwds[arg] = dialect_kwargs[arg]
    elif value == "default":  # Default --> no warning.
        from pandas.io.parsers.base_parser import parser_defaults

        kwds[arg] = parser_defaults[arg]
    else:  # Non-default + conflict with dialect --> warning.
        warning_klass = ParserWarning
        kwds[arg] = "blah"

with tm.with_csv_dialect(dialect_name, **dialect_kwargs):
    result = parser.read_csv_check_warnings(
        warning_klass,
        "Conflicting values for",
        StringIO(data),
        dialect=dialect_name,
        **kwds,
    )
    tm.assert_frame_equal(result, expected)
