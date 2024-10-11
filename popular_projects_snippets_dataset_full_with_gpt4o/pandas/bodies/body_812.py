# Extracted from ./data/repos/pandas/pandas/tests/internals/test_api.py
# GH#41168
dti = pd.date_range("2012", periods=3, tz="UTC")
blk = api.make_block(dti, placement=[0])

assert blk.shape == (1, 3)
assert blk.values.shape == (1, 3)
