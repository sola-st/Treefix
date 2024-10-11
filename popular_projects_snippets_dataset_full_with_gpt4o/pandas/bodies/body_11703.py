# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# see gh-10728, gh-10548
parser = all_parsers

if expected is None:
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data), **kwargs)
else:
    result = parser.read_csv(StringIO(data), **kwargs)
    tm.assert_frame_equal(result, expected)
