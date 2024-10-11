# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH#30892

dti = pd.to_datetime(["20190101", "20190101", "20190102"])
idx = Index(["a", "a", "c"])
mi = MultiIndex.from_arrays([dti, idx], names=["index1", "index2"])

df = DataFrame({"c1": [1, 2, 3], "c2": [np.nan, np.nan, np.nan]}, index=mi)

expected = DataFrame({"c1": df["c1"], "c2": [1.0, 1.0, np.nan]}, index=mi)

df2 = df.copy(deep=True)
df2.loc[(dti[0], "a"), "c2"] = 1.0
tm.assert_frame_equal(df2, expected)

df3 = df.copy(deep=True)
df3.loc[[(dti[0], "a")], "c2"] = 1.0
tm.assert_frame_equal(df3, expected)
