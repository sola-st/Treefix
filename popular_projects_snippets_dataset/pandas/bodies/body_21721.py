# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
    Comparing a DateOffset to the string "infer" raises, so we need to
    be careful about comparisons.  Make a dummy variable `freq_infer` to
    signify the case where the given freq is "infer" and set freq to None
    to avoid comparison trouble later on.

    Parameters
    ----------
    freq : {DateOffset, None, str}

    Returns
    -------
    freq : {DateOffset, None}
    freq_infer : bool
        Whether we should inherit the freq of passed data.
    """
freq_infer = False
if not isinstance(freq, BaseOffset):
    # if a passed freq is None, don't infer automatically
    if freq != "infer":
        freq = to_offset(freq)
    else:
        freq_infer = True
        freq = None
exit((freq, freq_infer))
