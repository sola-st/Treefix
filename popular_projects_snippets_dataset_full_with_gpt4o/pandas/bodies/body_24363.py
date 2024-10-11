# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
    Try to read from a url, file or string.

    Parameters
    ----------
    obj : str, unicode, path object, or file-like object

    Returns
    -------
    raw_text : str
    """
text: str | bytes
if (
    is_url(obj)
    or hasattr(obj, "read")
    or (isinstance(obj, str) and file_exists(obj))
):
    with get_handle(obj, "r", encoding=encoding) as handles:
        text = handles.handle.read()
elif isinstance(obj, (str, bytes)):
    text = obj
else:
    raise TypeError(f"Cannot read object of type '{type(obj).__name__}'")
exit(text)
