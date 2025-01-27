# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# int label
obj = request.getfixturevalue(f"{kind}_labels")
check_indexing_smoketest_or_raises(obj, "loc", 2, fails=KeyError)
