# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# see gh-24130
parser = all_parsers
encoding = encoding_fmt.format(utf_value)

expected = DataFrame({"foo": ["bar"]})

with tm.ensure_clean(mode="w+", encoding=encoding, return_filelike=True) as f:
    f.write("foo\nbar")
    f.seek(0)

    result = parser.read_csv(f, encoding=encoding if pass_encoding else None)
    tm.assert_frame_equal(result, expected)
