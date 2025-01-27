# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# label
obj = request.getfixturevalue(f"{kind}_empty")
check_indexing_smoketest_or_raises(obj, "loc", "c", fails=KeyError)
