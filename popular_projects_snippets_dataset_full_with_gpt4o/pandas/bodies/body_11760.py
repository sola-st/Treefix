# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
parser = all_parsers
data = """A,B,C
1,2,3
4,5,6
7,8,9
1,2,3"""

with parser.read_csv(StringIO(data), chunksize=2) as reader:
    result = reader.get_chunk()

expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"])
tm.assert_frame_equal(result, expected)
