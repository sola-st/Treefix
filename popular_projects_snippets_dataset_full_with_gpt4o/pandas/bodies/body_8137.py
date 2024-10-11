# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
result = ensure_index_from_sequences(data, names)
tm.assert_index_equal(result, expected)
