# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-21141
parser = all_parsers

if not parser.low_memory:
    pytest.skip("This is a low-memory specific test")

data = """A,B,C
1,1,1,2
2,2,3,4
3,3,4,5
"""
result = parser.read_csv(StringIO(data), low_memory=True, index_col=0, nrows=0)
expected = DataFrame(columns=["A", "B", "C"])
tm.assert_frame_equal(result, expected)
