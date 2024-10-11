# Extracted from ./data/repos/pandas/pandas/core/arraylike.py
"""
    Fallback to the behavior we would get if we did not define __array_ufunc__.

    Notes
    -----
    We are assuming that `self` is among `inputs`.
    """
if not any(x is self for x in inputs):
    raise NotImplementedError

new_inputs = [x if x is not self else np.asarray(x) for x in inputs]

exit(getattr(ufunc, method)(*new_inputs, **kwargs))
