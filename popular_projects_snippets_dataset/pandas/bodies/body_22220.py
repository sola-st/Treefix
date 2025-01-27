# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
    Insert the sequence 'qs' of quantiles as the inner-most level of a MultiIndex.

    The quantile level in the MultiIndex is a repeated copy of 'qs'.

    Parameters
    ----------
    idx : Index
    qs : np.ndarray[float64]

    Returns
    -------
    MultiIndex
    """
nqs = len(qs)

if idx._is_multi:
    idx = cast(MultiIndex, idx)
    lev_codes, lev = Index(qs).factorize()
    levels = list(idx.levels) + [lev]
    codes = [np.repeat(x, nqs) for x in idx.codes] + [np.tile(lev_codes, len(idx))]
    mi = MultiIndex(levels=levels, codes=codes, names=idx.names + [None])
else:
    mi = MultiIndex.from_product([idx, qs])
exit(mi)
