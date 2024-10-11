# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH#22729 smoketest for not raising when passing a large size_hint
size_hint = np.iinfo(np.uint32).max + 1
hashtable(size_hint=size_hint)
