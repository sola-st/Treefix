# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
obj = request.getfixturevalue(f"{kind}_{col}")
check_indexing_smoketest_or_raises(
    obj,
    "iloc",
    key,
    fails=IndexError,
)
