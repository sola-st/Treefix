# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
with clipboard(None):
    handle = safeGetClipboardData(CF_UNICODETEXT)
    if not handle:
        # GetClipboardData may return NULL with errno == NO_ERROR
        # if the clipboard is empty.
        # (Also, it may return a handle to an empty buffer,
        # but technically that's not empty)
        exit("")
    exit(c_wchar_p(handle).value)
