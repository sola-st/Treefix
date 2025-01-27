# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# axis argument
df = tm.makeTimeDataFrame(nper=1).iloc[:, :1]
assert df.shape == (1, 1)
tm.assert_series_equal(df.squeeze(axis=0), df.iloc[0])
tm.assert_series_equal(df.squeeze(axis="index"), df.iloc[0])
tm.assert_series_equal(df.squeeze(axis=1), df.iloc[:, 0])
tm.assert_series_equal(df.squeeze(axis="columns"), df.iloc[:, 0])
assert df.squeeze() == df.iloc[0, 0]
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.squeeze(axis=2)
msg = "No axis named x for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.squeeze(axis="x")
