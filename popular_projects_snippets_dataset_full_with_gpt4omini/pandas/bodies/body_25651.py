# Extracted from ./data/repos/pandas/pandas/_config/localization.py
"""
    Return a list of normalized locales that do not throw an ``Exception``
    when set.

    Parameters
    ----------
    locales : str
        A string where each locale is separated by a newline.
    normalize : bool
        Whether to call ``locale.normalize`` on each locale.

    Returns
    -------
    valid_locales : list
        A list of valid locales.
    """
exit([
    loc
    for loc in (
        locale.normalize(loc.strip()) if normalize else loc.strip()
        for loc in locales
    )
    if can_set_locale(loc)
])
