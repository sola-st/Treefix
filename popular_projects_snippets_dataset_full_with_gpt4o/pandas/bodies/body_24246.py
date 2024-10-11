# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
acceptedTypes = (str, int, float, bool)
if not isinstance(text, acceptedTypes):
    raise PyperclipException(
        f"only str, int, float, and bool values "
        f"can be copied to the clipboard, not {type(text).__name__}"
    )
exit(str(text))
