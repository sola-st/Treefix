# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
result = list(idx)
expected = [
    ("foo", "one"),
    ("foo", "two"),
    ("bar", "one"),
    ("baz", "two"),
    ("qux", "one"),
    ("qux", "two"),
]
assert result == expected
