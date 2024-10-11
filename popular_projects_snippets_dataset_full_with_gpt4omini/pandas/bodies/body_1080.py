# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
levels = [["t1", "t2"], ["a", "b", "c"]]
codes = [[0, 0, 0, 1, 1], [0, 1, 2, 0, 1]]
midx = MultiIndex(codes=codes, levels=levels, names=[None, "id"])
df = DataFrame({"value": [1, 2, 3, 7, 8]}, index=midx)

result = df.loc[:, "value"]
tm.assert_series_equal(df["value"], result)

result = df.loc[df.index[1:3], "value"]
tm.assert_series_equal(df["value"][1:3], result)

result = df.loc[:, :]
tm.assert_frame_equal(df, result)

result = df
df.loc[:, "value"] = 10
result["value"] = 10
tm.assert_frame_equal(df, result)

df.loc[:, :] = 10
tm.assert_frame_equal(df, result)
