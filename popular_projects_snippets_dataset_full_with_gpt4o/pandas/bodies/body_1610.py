# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#23462 key list of bools, value is a Series
td1 = Timedelta(0)
td2 = Timedelta(28767471428571405)
df = DataFrame({"col": Series([td1, td2])})
df_copy = df.copy()
ser = Series([td1])

expected = df["col"].iloc[1].value
df.loc[[True, False]] = ser
result = df["col"].iloc[1].value

assert expected == result
tm.assert_frame_equal(df, df_copy)
