# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = """\
1,2,3
4,5,6
7,8,9
10,11,12"""
parser = all_parsers
msg = "Number of passed names did not match number of header fields in the file"

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), names=["a", "b"], header=None, usecols=[1])
