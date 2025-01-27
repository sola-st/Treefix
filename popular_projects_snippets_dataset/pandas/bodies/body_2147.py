# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 21697
expected = Index([15e9] * 2, name="name")
result = to_datetime(expected, errors="ignore", unit="s", cache=cache)
tm.assert_index_equal(result, expected)
