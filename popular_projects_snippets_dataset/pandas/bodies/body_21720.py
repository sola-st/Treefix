# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
    If the user passes a freq and another freq is inferred from passed data,
    require that they match.

    Parameters
    ----------
    freq : DateOffset or None
    inferred_freq : DateOffset or None
    freq_infer : bool

    Returns
    -------
    freq : DateOffset or None
    freq_infer : bool

    Notes
    -----
    We assume at this point that `maybe_infer_freq` has been called, so
    `freq` is either a DateOffset object or None.
    """
if inferred_freq is not None:
    if freq is not None and freq != inferred_freq:
        raise ValueError(
            f"Inferred frequency {inferred_freq} from passed "
            "values does not conform to passed frequency "
            f"{freq.freqstr}"
        )
    if freq is None:
        freq = inferred_freq
    freq_infer = False

exit((freq, freq_infer))
