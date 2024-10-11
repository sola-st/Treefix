# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
# see gh-22789.
parser = all_parsers
data = 'a,b,c\n1,2,"3'

if balanced:
    # Re-balance the quoting and read in without errors.
    expected = DataFrame([[1, 2, 3]], columns=["a", "b", "c"])
    result = parser.read_csv(StringIO(data + '"'))
    tm.assert_frame_equal(result, expected)
else:
    msg = (
        "EOF inside string starting at row 1"
        if parser.engine == "c"
        else "unexpected end of data"
    )

    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data))
