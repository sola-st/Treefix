# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(parser)
a = np.random.choice(["red", "green"], size=10)
b = np.random.choice(["eggs", "ham"], size=10)
index = MultiIndex.from_arrays([a, b])
df = DataFrame(np.random.randn(10, 2), index=index)
ind = Series(df.index.get_level_values(0).values, index=index)

res1 = df.query('ilevel_0 == "red"', parser=parser, engine=engine)
res2 = df.query('"red" == ilevel_0', parser=parser, engine=engine)
exp = df[ind == "red"]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# inequality
res1 = df.query('ilevel_0 != "red"', parser=parser, engine=engine)
res2 = df.query('"red" != ilevel_0', parser=parser, engine=engine)
exp = df[ind != "red"]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# list equality (really just set membership)
res1 = df.query('ilevel_0 == ["red"]', parser=parser, engine=engine)
res2 = df.query('["red"] == ilevel_0', parser=parser, engine=engine)
exp = df[ind.isin(["red"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

res1 = df.query('ilevel_0 != ["red"]', parser=parser, engine=engine)
res2 = df.query('["red"] != ilevel_0', parser=parser, engine=engine)
exp = df[~ind.isin(["red"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# in/not in ops
res1 = df.query('["red"] in ilevel_0', parser=parser, engine=engine)
res2 = df.query('"red" in ilevel_0', parser=parser, engine=engine)
exp = df[ind.isin(["red"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

res1 = df.query('["red"] not in ilevel_0', parser=parser, engine=engine)
res2 = df.query('"red" not in ilevel_0', parser=parser, engine=engine)
exp = df[~ind.isin(["red"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# ## LEVEL 1
ind = Series(df.index.get_level_values(1).values, index=index)
res1 = df.query('ilevel_1 == "eggs"', parser=parser, engine=engine)
res2 = df.query('"eggs" == ilevel_1', parser=parser, engine=engine)
exp = df[ind == "eggs"]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# inequality
res1 = df.query('ilevel_1 != "eggs"', parser=parser, engine=engine)
res2 = df.query('"eggs" != ilevel_1', parser=parser, engine=engine)
exp = df[ind != "eggs"]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# list equality (really just set membership)
res1 = df.query('ilevel_1 == ["eggs"]', parser=parser, engine=engine)
res2 = df.query('["eggs"] == ilevel_1', parser=parser, engine=engine)
exp = df[ind.isin(["eggs"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

res1 = df.query('ilevel_1 != ["eggs"]', parser=parser, engine=engine)
res2 = df.query('["eggs"] != ilevel_1', parser=parser, engine=engine)
exp = df[~ind.isin(["eggs"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

# in/not in ops
res1 = df.query('["eggs"] in ilevel_1', parser=parser, engine=engine)
res2 = df.query('"eggs" in ilevel_1', parser=parser, engine=engine)
exp = df[ind.isin(["eggs"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)

res1 = df.query('["eggs"] not in ilevel_1', parser=parser, engine=engine)
res2 = df.query('"eggs" not in ilevel_1', parser=parser, engine=engine)
exp = df[~ind.isin(["eggs"])]
tm.assert_frame_equal(res1, exp)
tm.assert_frame_equal(res2, exp)
