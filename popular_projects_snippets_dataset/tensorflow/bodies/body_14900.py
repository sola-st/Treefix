# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Note that currently it just forwards to the numpy namesake, while
  tensorflow and numpy dtypes may have different properties."""
exit(np.finfo(_to_numpy_type(dtype)))
