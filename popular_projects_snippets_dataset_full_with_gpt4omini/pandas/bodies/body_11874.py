# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# see gh-6114
data = """\
MyColumn
   a
   b
   a
   b"""

msg = "Passing a bool to header is invalid"
with pytest.raises(TypeError, match=msg):
    read_fwf(StringIO(data), header=header)
