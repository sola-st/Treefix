# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
for typ in typs:
    obj = request.getfixturevalue(f"{kind}_{typ}")
    # list of labels
    check_indexing_smoketest_or_raises(obj, "loc", key, fails=KeyError)
