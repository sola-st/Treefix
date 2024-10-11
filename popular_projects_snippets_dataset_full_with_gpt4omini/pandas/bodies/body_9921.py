# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
# GH 10565
s = Series(np.arange(100), name="foo")

s2 = s.rolling(30).sum()
s3 = s.rolling(20).sum()
assert s2.name == "foo"
assert s3.name == "foo"
