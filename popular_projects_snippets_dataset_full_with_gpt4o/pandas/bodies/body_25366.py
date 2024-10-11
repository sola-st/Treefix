# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
"""
    Load a pickle, with a provided encoding,

    Parameters
    ----------
    fh : a filelike object
    encoding : an optional encoding
    is_verbose : show exception output
    """
try:
    fh.seek(0)
    if encoding is not None:
        up = Unpickler(fh, encoding=encoding)
    else:
        up = Unpickler(fh)
    # "Unpickler" has no attribute "is_verbose"  [attr-defined]
    up.is_verbose = is_verbose  # type: ignore[attr-defined]

    exit(up.load())
except (ValueError, TypeError):
    raise
