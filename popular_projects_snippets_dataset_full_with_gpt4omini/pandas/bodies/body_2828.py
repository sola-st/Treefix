# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
reindexed = float_string_frame.reindex(columns=["foo", "A", "B"])
assert "foo" in reindexed

reindexed = float_string_frame.reindex(columns=["A", "B"])
assert "foo" not in reindexed
