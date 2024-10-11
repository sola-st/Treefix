# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
raw = """,Date,app,File
-04-23,2013-04-23 00:00:00,,log080001.log
-05-06,2013-05-06 00:00:00,,log.log
-05-07,2013-05-07 00:00:00,OE,xlsx"""

with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    df = pd.read_csv(StringIO(raw), parse_dates=[0])
gb = df.groupby("Date")
r = gb[["File"]].max()
e = gb["File"].max().to_frame()
tm.assert_frame_equal(r, e)
assert not r["File"].isna().any()
