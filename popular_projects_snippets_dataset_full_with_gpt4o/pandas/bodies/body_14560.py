# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
# PR #25040 wide unicode wasn't copied correctly on PY3 on windows
clipboard_set(data)
assert data == clipboard_get()
