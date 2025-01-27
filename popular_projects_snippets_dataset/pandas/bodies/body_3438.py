# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
stacked = float_frame.stack()[::2]
stacked = DataFrame({"foo": stacked, "bar": stacked})

names = ["first", "second"]
stacked.index.names = names
deleveled = stacked.reset_index()
for i, (lev, level_codes) in enumerate(
    zip(stacked.index.levels, stacked.index.codes)
):
    values = lev.take(level_codes)
    name = names[i]
    tm.assert_index_equal(values, Index(deleveled[name]))

stacked.index.names = [None, None]
deleveled2 = stacked.reset_index()
tm.assert_series_equal(
    deleveled["first"], deleveled2["level_0"], check_names=False
)
tm.assert_series_equal(
    deleveled["second"], deleveled2["level_1"], check_names=False
)

# default name assigned
rdf = float_frame.reset_index()
exp = Series(float_frame.index.values, name="index")
tm.assert_series_equal(rdf["index"], exp)

# default name assigned, corner case
df = float_frame.copy()
df["index"] = "foo"
rdf = df.reset_index()
exp = Series(float_frame.index.values, name="level_0")
tm.assert_series_equal(rdf["level_0"], exp)

# but this is ok
float_frame.index.name = "index"
deleveled = float_frame.reset_index()
tm.assert_series_equal(deleveled["index"], Series(float_frame.index))
tm.assert_index_equal(deleveled.index, Index(range(len(deleveled))), exact=True)

# preserve column names
float_frame.columns.name = "columns"
reset = float_frame.reset_index()
assert reset.columns.name == "columns"

# only remove certain columns
df = float_frame.reset_index().set_index(["index", "A", "B"])
rs = df.reset_index(["A", "B"])

tm.assert_frame_equal(rs, float_frame)

rs = df.reset_index(["index", "A", "B"])
tm.assert_frame_equal(rs, float_frame.reset_index())

rs = df.reset_index(["index", "A", "B"])
tm.assert_frame_equal(rs, float_frame.reset_index())

rs = df.reset_index("A")
xp = float_frame.reset_index().set_index(["index", "B"])
tm.assert_frame_equal(rs, xp)

# test resetting in place
df = float_frame.copy()
reset = float_frame.reset_index()
return_value = df.reset_index(inplace=True)
assert return_value is None
tm.assert_frame_equal(df, reset)

df = float_frame.reset_index().set_index(["index", "A", "B"])
rs = df.reset_index("A", drop=True)
xp = float_frame.copy()
del xp["A"]
xp = xp.set_index(["B"], append=True)
tm.assert_frame_equal(rs, xp)
