# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# gh-17131
# a boolean index should index like a boolean numpy array

df = DataFrame(
    np.random.random(size=(5, 10)),
    index=["alpha_0", "alpha_1", "alpha_2", "beta_0", "beta_1"],
)

mask = df.index.map(lambda x: "alpha" in x)
expected = df.loc[np.array(mask)]

result = df.loc[mask]
tm.assert_frame_equal(result, expected)

result = df.loc[mask.values]
tm.assert_frame_equal(result, expected)

result = df.loc[pd.array(mask, dtype="boolean")]
tm.assert_frame_equal(result, expected)
