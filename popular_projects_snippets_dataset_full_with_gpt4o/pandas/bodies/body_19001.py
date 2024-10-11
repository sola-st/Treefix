# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
"""
    Cast an expression inplace.

    Parameters
    ----------
    terms : Op
        The expression that should cast.
    acceptable_dtypes : list of acceptable numpy.dtype
        Will not cast if term's dtype in this list.
    dtype : str or numpy.dtype
        The dtype to cast to.
    """
dt = np.dtype(dtype)
for term in terms:
    if term.type in acceptable_dtypes:
        continue

    try:
        new_value = term.value.astype(dt)
    except AttributeError:
        new_value = dt.type(term.value)
    term.update(new_value)
