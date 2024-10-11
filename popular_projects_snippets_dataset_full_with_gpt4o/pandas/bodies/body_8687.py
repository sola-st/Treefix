# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
expected = pd.Categorical(result)
assert all(result == expected)
assert not any(result != expected)
