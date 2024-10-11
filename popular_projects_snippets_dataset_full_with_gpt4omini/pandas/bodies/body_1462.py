# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# fails
obj = request.getfixturevalue(f"{kind}_{typs}")
check_indexing_smoketest_or_raises(
    obj, "loc", [20, 30, 40], axes=1, fails=KeyError
)
