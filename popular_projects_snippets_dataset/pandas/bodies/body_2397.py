# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
arr = np.random.randn(5, 5)

df = DataFrame(arr.copy(), columns=["A", "B", "C", "D", "E"])

df[df < 0] += 1
arr[arr < 0] += 1

tm.assert_almost_equal(df.values, arr)
