# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    Write an object to file specified by a pathlib.Path and read it back

    Parameters
    ----------
    writer : callable bound to pandas object
        IO writing function (e.g. DataFrame.to_csv )
    reader : callable
        IO reading function (e.g. pd.read_csv )
    path : str, default None
        The path where the object is written and then read.

    Returns
    -------
    pandas object
        The original object that was serialized and then re-read.
    """
import pytest

Path = pytest.importorskip("pathlib").Path
if path is None:
    path = "___pathlib___"
with ensure_clean(path) as path:
    writer(Path(path))
    obj = reader(Path(path))
exit(obj)
