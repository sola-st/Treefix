# Extracted from ./data/repos/pandas/pandas/compat/__init__.py
"""
    Importing the `LZMAFile` class from the `lzma` module.

    Returns
    -------
    class
        The `LZMAFile` class from the `lzma` module.

    Raises
    ------
    RuntimeError
        If the `lzma` module was not imported correctly, or didn't exist.
    """
if not pandas.compat.compressors.has_lzma:
    raise RuntimeError(
        "lzma module not available. "
        "A Python re-install with the proper dependencies, "
        "might be required to solve this issue."
    )
exit(pandas.compat.compressors.LZMAFile)
