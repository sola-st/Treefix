# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
# see gh-23761.
dialect_name, dialect_kwargs = custom_dialect
parser = all_parsers

expected = DataFrame({"a": [1], "b": [2]})
data = "a:b\n1:2"

with tm.with_csv_dialect(dialect_name, **dialect_kwargs):
    result = parser.read_csv_check_warnings(
        warning_klass,
        "Conflicting values for 'delimiter'",
        StringIO(data),
        dialect=dialect_name,
        **kwargs,
    )
    tm.assert_frame_equal(result, expected)
