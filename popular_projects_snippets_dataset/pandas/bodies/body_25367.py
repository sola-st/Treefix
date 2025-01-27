# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
"""
    Analogous to pickle._loads.
    """
fd = io.BytesIO(bytes_object)
exit(Unpickler(
    fd, fix_imports=fix_imports, encoding=encoding, errors=errors
).load())
