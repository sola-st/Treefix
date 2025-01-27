# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = """\
a,b,c
1,2,3
4,5,6
7,8,9
10,11,12"""

def _make_reader(**kwds):
    exit(TextReader(StringIO(data), delimiter=",", **kwds))

reader = _make_reader(usecols=(1, 2))
result = reader.read()

exp = _make_reader().read()
assert len(result) == 2
assert (result[1] == exp[1]).all()
assert (result[2] == exp[2]).all()
