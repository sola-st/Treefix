# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_frame.py
# GH#44212 if we explicitly pass name=None, then that should be respected,
#  not changed to 0
# GH-45448 this is first deprecated to only change in the future
idx = date_range(start="2019-01-01", end="2019-01-30", freq="D", tz="UTC")
result = idx.to_frame(name=None)
exp_idx = Index([None], dtype=object)
tm.assert_index_equal(exp_idx, result.columns)

result = idx.rename("foo").to_frame(name=None)
exp_idx = Index([None], dtype=object)
tm.assert_index_equal(exp_idx, result.columns)
