# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
obj = request.getfixturevalue(f"{kind}_empty")
# boolean indexers
b = [True, False, True, False]

check_indexing_smoketest_or_raises(obj, "loc", b, fails=IndexError)
