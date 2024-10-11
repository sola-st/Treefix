# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
"""
    Gets a temporary path and agrees to remove on close.

    This implementation does not use tempfile.mkstemp to avoid having a file handle.
    If the code using the returned path wants to delete the file itself, windows
    requires that no program has a file handle to it.

    Parameters
    ----------
    filename : str (optional)
        suffix of the created file.
    return_filelike : bool (default False)
        if True, returns a file-like which is *always* cleaned. Necessary for
        savefig and other functions which want to append extensions.
    **kwargs
        Additional keywords are passed to open().

    """
folder = Path(tempfile.gettempdir())

if filename is None:
    filename = ""
filename = str(uuid.uuid4()) + filename
path = folder / filename

path.touch()

handle_or_str: str | IO = str(path)
if return_filelike:
    kwargs.setdefault("mode", "w+b")
    handle_or_str = open(path, **kwargs)

try:
    exit(handle_or_str)
finally:
    if not isinstance(handle_or_str, str):
        handle_or_str.close()
    if path.is_file():
        path.unlink()
