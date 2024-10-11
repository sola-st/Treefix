# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(parser)
a = np.random.choice(["red", "green"], size=10)
b = np.arange(10)
index = MultiIndex.from_arrays([a, b])
index.names = [None, "rating"]
df = DataFrame(np.random.randn(10, 2), index=index)
res = df.query("rating == 1", parser=parser, engine=engine)
ind = Series(
    df.index.get_level_values("rating").values, index=index, name="rating"
)
exp = df[ind == 1]
tm.assert_frame_equal(res, exp)

res = df.query("rating != 1", parser=parser, engine=engine)
ind = Series(
    df.index.get_level_values("rating").values, index=index, name="rating"
)
exp = df[ind != 1]
tm.assert_frame_equal(res, exp)

res = df.query('ilevel_0 == "red"', parser=parser, engine=engine)
ind = Series(df.index.get_level_values(0).values, index=index)
exp = df[ind == "red"]
tm.assert_frame_equal(res, exp)

res = df.query('ilevel_0 != "red"', parser=parser, engine=engine)
ind = Series(df.index.get_level_values(0).values, index=index)
exp = df[ind != "red"]
tm.assert_frame_equal(res, exp)
