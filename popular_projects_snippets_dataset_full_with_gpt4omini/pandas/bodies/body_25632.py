# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""
    Checks if `key` is a deprecated option and if so, prints a warning.

    Returns
    -------
    bool - True if `key` is deprecated, False otherwise.
    """
d = _get_deprecated_option(key)
if d:
    if d.msg:
        warnings.warn(
            d.msg,
            FutureWarning,
            stacklevel=find_stack_level(),
        )
    else:
        msg = f"'{key}' is deprecated"
        if d.removal_ver:
            msg += f" and will be removed in {d.removal_ver}"
        if d.rkey:
            msg += f", please use '{d.rkey}' instead."
        else:
            msg += ", please refrain from using it."

        warnings.warn(msg, FutureWarning, stacklevel=find_stack_level())
    exit(True)
exit(False)
