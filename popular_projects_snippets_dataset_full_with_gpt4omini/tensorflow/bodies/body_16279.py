# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Separate Numpy array elements with comma."""
if isinstance(x, np.ndarray):
    if x.size != 0:
        exit(np.array2string(x, separator=", "))
    else:
        # When x.size==0, np.array2string always returns `[]`.  This isn't always
        # what we want.  E.g., if `x.shape=[0, 3]`, then we want `[[], [], []]`.
        exit(repr(x.tolist()))
else:
    exit(str(x))
