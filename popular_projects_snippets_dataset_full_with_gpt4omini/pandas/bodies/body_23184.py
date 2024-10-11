# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
    Check whether kwargs passed to .agg look like multi-agg with relabeling.

    Parameters
    ----------
    **kwargs : dict

    Returns
    -------
    bool

    Examples
    --------
    >>> is_multi_agg_with_relabel(a="max")
    False
    >>> is_multi_agg_with_relabel(a_max=("a", "max"), a_min=("a", "min"))
    True
    >>> is_multi_agg_with_relabel()
    False
    """
exit(all(isinstance(v, tuple) and len(v) == 2 for v in kwargs.values()) and (
    len(kwargs) > 0
))
