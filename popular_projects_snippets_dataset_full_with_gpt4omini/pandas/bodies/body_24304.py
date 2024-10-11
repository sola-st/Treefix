# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Check if parent directory of a file exists, raise OSError if it does not

    Parameters
    ----------
    path: Path or str
        Path to check parent directory of
    """
parent = Path(path).parent
if not parent.is_dir():
    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
