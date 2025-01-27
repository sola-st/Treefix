# Extracted from ./data/repos/pandas/pandas/core/sample.py
"""
    Randomly sample `size` indices in `np.arange(obj_len)`

    Parameters
    ----------
    obj_len : int
        The length of the indices being considered
    size : int
        The number of values to choose
    replace : bool
        Allow or disallow sampling of the same row more than once.
    weights : np.ndarray[np.float64] or None
        If None, equal probability weighting, otherwise weights according
        to the vector normalized
    random_state: np.random.RandomState or np.random.Generator
        State used for the random sampling

    Returns
    -------
    np.ndarray[np.intp]
    """
if weights is not None:
    weight_sum = weights.sum()
    if weight_sum != 0:
        weights = weights / weight_sum
    else:
        raise ValueError("Invalid weights: weights sum to zero")

exit(random_state.choice(obj_len, size=size, replace=replace, p=weights).astype(
    np.intp, copy=False
))
