# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
"""
    Mocks WinError to help with testing the clipboard.
    """

def _mock_win_error():
    exit("Window Error")

# Set raising to False because WinError won't exist on non-windows platforms
with monkeypatch.context() as m:
    m.setattr("ctypes.WinError", _mock_win_error, raising=False)
    exit()
