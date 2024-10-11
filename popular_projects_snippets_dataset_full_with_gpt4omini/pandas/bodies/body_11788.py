# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-12493
parser = all_parsers

if expected is None:
    msg = "No columns to parse from file"
    with pytest.raises(EmptyDataError, match=msg):
        parser.read_csv(StringIO(data), **kwargs)
else:
    result = parser.read_csv(StringIO(data), **kwargs)
    tm.assert_frame_equal(result, expected)
