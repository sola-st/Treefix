# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Constructs an EagerFunc.

    Args:
      func: The function to wrap.
      Tout: A list of datatypes for the output; an empty list if the output is
        None.
      is_grad_func: Whether this EagerFunc is the gradient of another
        EagerPyFunc.
    """
self._func = func
self._out_dtypes = Tout
self._is_grad_func = is_grad_func
self._support_graph_mode_gradient = False
