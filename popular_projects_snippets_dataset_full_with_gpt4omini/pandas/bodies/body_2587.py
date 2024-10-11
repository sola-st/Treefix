# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# assign multiple rows (mixed values) (-> array) -> exp_multi_row
# changed multiple rows
cats2 = Categorical(["a", "a", "b", "b", "a", "a", "a"], categories=["a", "b"])
idx2 = Index(["h", "i", "j", "k", "l", "m", "n"])
values2 = [1, 1, 2, 2, 1, 1, 1]
exp_multi_row = DataFrame({"cats": cats2, "values": values2}, index=idx2)

catsf = Categorical(
    ["a", "a", "c", "c", "a", "a", "a"], categories=["a", "b", "c"]
)
idxf = Index(["h", "i", "j", "k", "l", "m", "n"])
valuesf = [1, 1, 3, 3, 1, 1, 1]
df = DataFrame({"cats": catsf, "values": valuesf}, index=idxf)

exp_fancy = exp_multi_row.copy()
exp_fancy["cats"] = exp_fancy["cats"].cat.set_categories(["a", "b", "c"])

mask = df["cats"] == "c"
df[mask] = ["b", 2]
# category c is kept in .categories
tm.assert_frame_equal(df, exp_fancy)
