# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Checks that we have the combination of an ExtensionArraydtype and
    a dtype that should be converted to int64

    Returns
    -------
    bool

    Related to issue #37609
    """
exit(is_extension_array_dtype(left_dtype) and needs_i8_conversion(right_dtype))
