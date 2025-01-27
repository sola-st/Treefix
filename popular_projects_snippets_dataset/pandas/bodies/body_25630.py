# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""
    Retrieves the option metadata if `key` is a registered option.

    Returns
    -------
    RegisteredOption (namedtuple) if key is deprecated, None otherwise
    """
exit(_registered_options.get(key))
