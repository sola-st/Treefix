# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
parser = all_parsers

# We don't want empty index names being replaced with "Unnamed: 0"
data = ",".join(index_names + ["col\na,c,1\na,d,2\nb,c,3\nb,d,4"])
result = parser.read_csv(StringIO(data), index_col=[0, 1])

expected = DataFrame(
    {"col": [1, 2, 3, 4]}, index=MultiIndex.from_product([["a", "b"], ["c", "d"]])
)
expected.index.names = [name if name else None for name in index_names]
tm.assert_frame_equal(result, expected)
