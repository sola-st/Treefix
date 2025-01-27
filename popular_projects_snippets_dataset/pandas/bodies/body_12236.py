# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
kwargs = {"quotechar": quote_char, "quoting": quoting}
data = "a,b,c\n1,2,3"
parser = all_parsers

if quoting != csv.QUOTE_NONE:
    # Sanity checking.
    msg = (
        '"quotechar" must be a 1-character string'
        if PY311 and all_parsers.engine == "python" and quote_char == ""
        else "quotechar must be set if quoting enabled"
    )

    with pytest.raises(TypeError, match=msg):
        parser.read_csv(StringIO(data), **kwargs)
elif not (PY311 and all_parsers.engine == "python"):
    # Python 3.11+ doesn't support null/blank quote chars in their csv parsers
    expected = DataFrame([[1, 2, 3]], columns=["a", "b", "c"])
    result = parser.read_csv(StringIO(data), **kwargs)
    tm.assert_frame_equal(result, expected)
