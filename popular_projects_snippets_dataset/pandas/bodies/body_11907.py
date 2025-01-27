# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# GH 10984
parser = all_parsers
midx = MultiIndex.from_tuples([("A", 1, 2), ("A", 1, 2), ("B", 1, 2)])
expected = DataFrame(np.random.randn(3, 3), index=midx, columns=["x", "y", "z"])
with tm.ensure_clean() as path:
    expected.to_csv(path)
    result = parser.read_csv(path, index_col=[0, 1, 2])
tm.assert_frame_equal(result, expected)
