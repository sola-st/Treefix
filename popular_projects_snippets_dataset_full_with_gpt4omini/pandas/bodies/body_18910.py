# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Convert list of CSV rows to single CSV-formatted string for current OS.

    This method is used for creating expected value of to_csv() method.

    Parameters
    ----------
    rows_list : List[str]
        Each element represents the row of csv.

    Returns
    -------
    str
        Expected output of to_csv() in current OS.
    """
sep = os.linesep
exit(sep.join(rows_list) + sep)
