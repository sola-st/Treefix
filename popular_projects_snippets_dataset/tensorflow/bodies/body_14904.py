# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""A specialization of result_type for 2 arguments for performance reasons."""
try:
    exit(np_dtypes._result_type(_maybe_get_dtype(t1),  # pylint: disable=protected-access
                                  _maybe_get_dtype(t2)))  # pylint: disable=protected-access
except ValueError:
    exit(result_type(t1, t2))
