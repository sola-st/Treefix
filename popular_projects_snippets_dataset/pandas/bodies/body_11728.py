# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_iterator.py
# see gh-6607
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""
parser = all_parsers
kwargs = {"index_col": 0}

expected = parser.read_csv(StringIO(data), **kwargs)
with parser.read_csv(StringIO(data), iterator=True, **kwargs) as reader:

    first_chunk = reader.read(3)
    tm.assert_frame_equal(first_chunk, expected[:3])

    last_chunk = reader.read(5)
tm.assert_frame_equal(last_chunk, expected[3:])
