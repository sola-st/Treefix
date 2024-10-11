# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#45580
df = DataFrame(index=date_range("2021", "2022"))
result = df.loc[np.array(["2021/6/1"])[0] :]
expected = df.iloc[151:]
tm.assert_frame_equal(result, expected)
