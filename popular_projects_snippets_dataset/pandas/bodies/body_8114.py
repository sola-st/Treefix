# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
df = pd.read_csv(StringIO("a,b,c\n1,2,3\n4,5,6"), index_col=[0, 1])

result = df.index == df.index
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
