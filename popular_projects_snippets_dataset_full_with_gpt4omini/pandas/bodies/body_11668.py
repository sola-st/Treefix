# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
parser = all_parsers
expected = DataFrame(
    np.array([[2, 3, 4, 5, 6], [8, 9, 10, 11, 12]], dtype="int64"),
    index=Index([1, 7]),
    columns=MultiIndex(
        levels=[["a", "b", "c"], ["r", "s", "t", "u", "v"]],
        codes=[[0, 0, 1, 2, 2], [0, 1, 2, 3, 4]],
        names=["a", "q"],
    ),
)
data = """a,a,a,b,c,c
q,r,s,t,u,v
1,2,3,4,5,6
7,8,9,10,11,12"""

result = parser.read_csv(StringIO(data), header=[0, 1], index_col=0)
tm.assert_frame_equal(expected, result)
