# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH9785
# test comparisons of multiindex
df = pd.read_csv(StringIO("a,b,c\n1,2,3\n4,5,6"), index_col=[0, 1])

result = df.index == mi
tm.assert_numpy_array_equal(result, expected)
