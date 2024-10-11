# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py

cat = Categorical([1, 2, 3, np.nan], categories=[1, 2, 3])
vals = ["a", "b", np.nan, "d"]
df = DataFrame({"cats": cat, "vals": vals})
cat2 = Categorical([1, 2, 3, 3], categories=[1, 2, 3])
vals2 = ["a", "b", "b", "d"]
df_exp_fill = DataFrame({"cats": cat2, "vals": vals2})
cat3 = Categorical([1, 2, 3], categories=[1, 2, 3])
vals3 = ["a", "b", np.nan]
df_exp_drop_cats = DataFrame({"cats": cat3, "vals": vals3})
cat4 = Categorical([1, 2], categories=[1, 2, 3])
vals4 = ["a", "b"]
df_exp_drop_all = DataFrame({"cats": cat4, "vals": vals4})

# fillna
res = df.fillna(value={"cats": 3, "vals": "b"})
tm.assert_frame_equal(res, df_exp_fill)

msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    df.fillna(value={"cats": 4, "vals": "c"})

res = df.fillna(method="pad")
tm.assert_frame_equal(res, df_exp_fill)

# dropna
res = df.dropna(subset=["cats"])
tm.assert_frame_equal(res, df_exp_drop_cats)

res = df.dropna()
tm.assert_frame_equal(res, df_exp_drop_all)

# make sure that fillna takes missing values into account
c = Categorical([np.nan, "b", np.nan], categories=["a", "b"])
df = DataFrame({"cats": c, "vals": [1, 2, 3]})

cat_exp = Categorical(["a", "b", "a"], categories=["a", "b"])
df_exp = DataFrame({"cats": cat_exp, "vals": [1, 2, 3]})

res = df.fillna("a")
tm.assert_frame_equal(res, df_exp)
