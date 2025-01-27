# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# see gh-2741
data = "\x00,foo"
names = ["a", "b"]
parser = all_parsers

if parser.engine == "c" or (parser.engine == "python" and PY311):
    if parser.engine == "python" and PY311:
        request.node.add_marker(
            pytest.mark.xfail(
                reason="In Python 3.11, this is read as an empty character not null"
            )
        )
    expected = DataFrame([[np.nan, "foo"]], columns=names)
    out = parser.read_csv(StringIO(data), names=names)
    tm.assert_frame_equal(out, expected)
else:
    msg = "NULL byte detected"
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data), names=names)
