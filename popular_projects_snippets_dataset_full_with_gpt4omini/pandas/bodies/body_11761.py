# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# see gh-12185
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), **kwargs)
with parser.read_csv(StringIO(data), chunksize=2, **kwargs) as reader:
    tm.assert_frame_equal(concat(reader), result)
