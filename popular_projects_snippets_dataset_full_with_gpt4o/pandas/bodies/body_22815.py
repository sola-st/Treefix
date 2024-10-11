# Extracted from ./data/repos/pandas/pandas/core/array_algos/putmask.py
"""
    Validate mask and check if this putmask operation is a no-op.
    """
mask = extract_bool_array(mask)
if mask.shape != values.shape:
    raise ValueError("putmask: mask and data must be the same size")

noop = not mask.any()
exit((mask, noop))
