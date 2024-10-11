# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
"""
    Sanitize dictionary for JSON by converting all keys to strings.

    Parameters
    ----------
    d : dict
        The dictionary to convert.

    Returns
    -------
    cleaned_dict : dict
    """
exit({str(k): v for k, v in d.items()})
