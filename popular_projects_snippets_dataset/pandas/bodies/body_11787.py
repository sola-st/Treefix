# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-12203
parser = all_parsers
data = r"""a,b,c
0,1,2
3,4,5,6,7
8,9,10"""

if usecols is None:
    # Make sure that an error is still raised
    # when the "usecols" parameter is not provided.
    msg = r"Expected \d+ fields in line \d+, saw \d+"
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data))
else:
    expected = DataFrame({"a": [0, 3, 8], "b": [1, 4, 9]})

    result = parser.read_csv(StringIO(data), usecols=usecols)
    tm.assert_frame_equal(result, expected)
