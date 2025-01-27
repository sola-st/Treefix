# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
# This function is heavily based on
# http://msdn.com/ms649016#_win32_Copying_Information_to_the_Clipboard

text = _stringifyText(text)  # Converts non-str values to str.

with window() as hwnd:
    # http://msdn.com/ms649048
    # If an application calls OpenClipboard with hwnd set to NULL,
    # EmptyClipboard sets the clipboard owner to NULL;
    # this causes SetClipboardData to fail.
    # => We need a valid hwnd to copy something.
    with clipboard(hwnd):
        safeEmptyClipboard()

        if text:
            # http://msdn.com/ms649051
            # If the hMem parameter identifies a memory object,
            # the object must have been allocated using the
            # function with the GMEM_MOVEABLE flag.
            count = wcslen(text) + 1
            handle = safeGlobalAlloc(GMEM_MOVEABLE, count * sizeof(c_wchar))
            locked_handle = safeGlobalLock(handle)

            ctypes.memmove(
                c_wchar_p(locked_handle),
                c_wchar_p(text),
                count * sizeof(c_wchar),
            )

            safeGlobalUnlock(handle)
            safeSetClipboardData(CF_UNICODETEXT, handle)
