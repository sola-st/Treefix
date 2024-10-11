# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH 25509
colname = "\ud83d"
df = DataFrame({colname: []})
# this should not crash
assert colname not in dir(df)
assert df.columns[0] == colname
