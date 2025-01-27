# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_get.py
# see gh-5652
assert df.get(None) is None
