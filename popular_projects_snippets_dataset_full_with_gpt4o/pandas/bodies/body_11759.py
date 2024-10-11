# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""
parser = all_parsers
kwargs = {"index_col": 0, "nrows": 5}

expected = parser.read_csv(StringIO(data), **kwargs)
with parser.read_csv(StringIO(data), chunksize=8, **kwargs) as reader:
    tm.assert_frame_equal(reader.get_chunk(size=2), expected.iloc[:2])
    tm.assert_frame_equal(reader.get_chunk(size=4), expected.iloc[2:5])

    with pytest.raises(StopIteration, match=""):
        reader.get_chunk(size=3)
