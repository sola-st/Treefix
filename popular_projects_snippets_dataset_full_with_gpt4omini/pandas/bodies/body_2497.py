# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#39614
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
indexer = (x for x in [1, 2])
result = df.iloc[indexer]
expected = DataFrame({"a": [2, 3], "b": [5, 6]}, index=[1, 2])
tm.assert_frame_equal(result, expected)
