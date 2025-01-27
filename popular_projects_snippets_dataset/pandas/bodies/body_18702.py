# Extracted from ./data/repos/pandas/pandas/conftest.py
"""Ignore doctest warning.

    Parameters
    ----------
    item : pytest.Item
        pytest test item.
    path : str
        Module path to Python object, e.g. "pandas.core.frame.DataFrame.append". A
        warning will be filtered when item.name ends with in given path. So it is
        sufficient to specify e.g. "DataFrame.append".
    message : str
        Message to be filtered.
    """
if item.name.endswith(path):
    item.add_marker(pytest.mark.filterwarnings(f"ignore:{message}"))
