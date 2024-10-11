# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#1048
df = DataFrame({"c": [Timestamp("2010-10-01")] * 3})
df.loc[0:1, "c"] = np.datetime64("2008-08-08")
assert Timestamp("2008-08-08") == df.loc[0, "c"]
assert Timestamp("2008-08-08") == df.loc[1, "c"]
df.loc[2, "c"] = date(2005, 5, 5)
assert Timestamp("2005-05-05").date() == df.loc[2, "c"]
