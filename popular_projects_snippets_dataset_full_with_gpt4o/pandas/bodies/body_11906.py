# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
parser = all_parsers
data = ",Unnamed: 2,\na,c,1\na,d,2\nb,c,3\nb,d,4"
result = parser.read_csv(StringIO(data), index_col=[0, 2])

expected = DataFrame(
    {"Unnamed: 2": ["c", "d", "c", "d"]},
    index=MultiIndex(
        levels=[["a", "b"], [1, 2, 3, 4]], codes=[[0, 0, 1, 1], [0, 1, 2, 3]]
    ),
)
tm.assert_frame_equal(result, expected)
