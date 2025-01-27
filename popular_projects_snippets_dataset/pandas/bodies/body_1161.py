# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH 38015
mi = MultiIndex.from_tuples([("A", "cat"), ("B", "cat"), ("B", "cat")])
df = DataFrame(index=mi)
df = df.rename(index={"A": "Apple"}, level=0)

mi2 = MultiIndex.from_tuples([("Apple", "cat"), ("B", "cat"), ("B", "cat")])
expected = DataFrame(index=mi2)
tm.assert_frame_equal(df, expected)
