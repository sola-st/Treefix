# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
import pandas.io.clipboard

pandas.io.clipboard.clipboard_set("abc")
assert "abc" in set(mock_clipboard.values())
result = pandas.io.clipboard.clipboard_get()
assert result == "abc"
