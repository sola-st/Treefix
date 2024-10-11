# Extracted from ./data/repos/pandas/pandas/_config/localization.py
"""
    Check to see if we can set a locale, and subsequently get the locale,
    without raising an Exception.

    Parameters
    ----------
    lc : str
        The locale to attempt to set.
    lc_var : int, default `locale.LC_ALL`
        The category of the locale being set.

    Returns
    -------
    bool
        Whether the passed locale can be set
    """
try:
    with set_locale(lc, lc_var=lc_var):
        pass
except (ValueError, locale.Error):
    # horrible name for a Exception subclass
    exit(False)
else:
    exit(True)
