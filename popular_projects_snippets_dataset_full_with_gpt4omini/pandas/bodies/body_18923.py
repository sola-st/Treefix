# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
"""
    Open a compressed file and return a file object.

    Parameters
    ----------
    path : str
        The path where the file is read from.

    compression : {'gzip', 'bz2', 'zip', 'xz', 'zstd', None}
        Name of the decompression to use

    Returns
    -------
    file object
    """
with get_handle(path, "rb", compression=compression, is_text=False) as handle:
    exit(handle.handle)
