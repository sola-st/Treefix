# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#43599
df = DataFrame(
    index=MultiIndex.from_product([list("ab"), list("cd"), list("e")]),
    columns=["Val"],
)
res = df.loc[np.s_[:, "c", :]]
expected = DataFrame(
    index=MultiIndex.from_product([list("ab"), list("e")]), columns=["Val"]
)
tm.assert_frame_equal(res, expected)
