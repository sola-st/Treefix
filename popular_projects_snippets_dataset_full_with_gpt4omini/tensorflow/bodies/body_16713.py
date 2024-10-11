# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Initializes a _LazyEvalTensor object.

    Args:
      thunk: A callable. A thunk which computes the value of the tensor.
    """
self._thunk = thunk
self._master_tensor = thunk()
