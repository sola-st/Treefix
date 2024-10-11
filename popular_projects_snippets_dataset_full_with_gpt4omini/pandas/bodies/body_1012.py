# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py

# GH29519
df = DataFrame(
    np.arange(27).reshape(3, 9),
    columns=MultiIndex.from_product([["a1", "a2", "a3"], ["b1", "b2", "b3"]]),
)
result = df.loc(axis=1)["a1"]
expected = df.iloc[:, :3]
expected.columns = ["b1", "b2", "b3"]

tm.assert_frame_equal(result, expected)
