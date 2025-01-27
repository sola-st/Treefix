# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#16979
data = np.arange(2 * 3, dtype=np.int64).reshape(2, 3)
df = DataFrame(data, columns=list("ABC"))
mask = np.array([[True, False, False], [False, False, True]])

# change type to category
df.A = df.A.astype("category")
df.B = df.B.astype("category")
df.C = df.C.astype("category")

result = df.where(mask, **kwargs)
A = pd.Categorical([0, np.nan], categories=[0, 3])
B = pd.Categorical([np.nan, np.nan], categories=[1, 4])
C = pd.Categorical([np.nan, 5], categories=[2, 5])
expected = DataFrame({"A": A, "B": B, "C": C})

tm.assert_frame_equal(result, expected)

# Check Series.where while we're here
result = df.A.where(mask[:, 0], **kwargs)
expected = Series(A, name="A")

tm.assert_series_equal(result, expected)
