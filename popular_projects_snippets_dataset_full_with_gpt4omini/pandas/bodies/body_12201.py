# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = "a,b,c,d\n1,2,3,4\n5,6,7,8"
kwargs.update(usecols=usecols)
parser = all_parsers

if expected is None:
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), **kwargs)
else:
    result = parser.read_csv(StringIO(data), **kwargs)
    tm.assert_frame_equal(result, expected)
