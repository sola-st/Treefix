# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""

msg = "column specifications must be a list or tuple.+"

with pytest.raises(TypeError, match=msg):
    read_fwf(StringIO(data), colspecs={"a": 1}, delimiter=",")
