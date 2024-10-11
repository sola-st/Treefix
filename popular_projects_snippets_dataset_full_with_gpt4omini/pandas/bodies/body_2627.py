# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
df = tm.SubclassedDataFrame(
    {"X": [1, 2, 3], "Y": [1, 2, 3]}, index=["a", "b", "c"]
)
df.testattr = "XXX"

assert df.testattr == "XXX"
assert df[["X"]].testattr == "XXX"
assert df.loc[["a", "b"], :].testattr == "XXX"
assert df.iloc[[0, 1], :].testattr == "XXX"

# see gh-9776
assert df.iloc[0:1, :].testattr == "XXX"

# see gh-10553
unpickled = tm.round_trip_pickle(df)
tm.assert_frame_equal(df, unpickled)
assert df._metadata == unpickled._metadata
assert df.testattr == unpickled.testattr
