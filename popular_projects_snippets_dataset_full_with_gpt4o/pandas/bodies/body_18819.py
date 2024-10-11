# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    Pickle an object and then read it again.

    Parameters
    ----------
    obj : any object
        The object to pickle and then re-read.
    path : str, path object or file-like object, default None
        The path where the pickled object is written and then read.

    Returns
    -------
    pandas object
        The original object that was pickled and then re-read.
    """
_path = path
if _path is None:
    _path = f"__{rands(10)}__.pickle"
with ensure_clean(_path) as temp_path:
    pd.to_pickle(obj, temp_path)
    exit(pd.read_pickle(temp_path))
