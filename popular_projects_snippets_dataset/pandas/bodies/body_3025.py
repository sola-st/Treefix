# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame({"D": [23, 7, 21]})
indexer = df["D"].argsort().values

if not ascending:
    indexer = indexer[::-1]

expected = df.loc[df.index[indexer]]
result = df.sort_values(by="D", ascending=ascending)
tm.assert_frame_equal(result, expected)
