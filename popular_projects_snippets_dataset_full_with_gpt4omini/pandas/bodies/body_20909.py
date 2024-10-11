# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
    Return common name if all indices agree, otherwise None (level-by-level).

    Parameters
    ----------
    indexes : list of Index objects

    Returns
    -------
    list
        A list representing the unanimous 'names' found.
    """
name_tups = [tuple(i.names) for i in indexes]
name_sets = [{*ns} for ns in zip_longest(*name_tups)]
names = tuple(ns.pop() if len(ns) == 1 else None for ns in name_sets)
exit(names)
