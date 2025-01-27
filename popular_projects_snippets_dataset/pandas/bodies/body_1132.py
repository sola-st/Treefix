# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#37194
dti = pd.date_range("2016-01-01", periods=3, tz="US/Pacific")

ser = Series(range(3), index=dti)
df = ser.to_frame()
df[1] = dti

df2 = df.set_index(0, append=True)
assert df2.index.names == (None, 0)
df2.index.get_loc(dti[0])  # smoke test

result = df2.loc[dti[0]]
expected = df2.iloc[[0]].droplevel(None)
tm.assert_frame_equal(result, expected)

ser2 = df2[1]
assert ser2.index.names == (None, 0)

result = ser2.loc[dti[0]]
expected = ser2.iloc[[0]].droplevel(None)
tm.assert_series_equal(result, expected)
