# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
expected = index.copy()
if name:
    expected.name = name

result = expected.get_level_values(level)
tm.assert_index_equal(result, expected)
