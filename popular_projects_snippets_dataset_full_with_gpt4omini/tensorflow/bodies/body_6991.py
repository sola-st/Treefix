# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Initialize an output context.

    Returns:
      A context object.
    """
self._last_step_outputs = {}
self._last_step_outputs_reduce_ops = {}
self._non_tensor_outputs = {}
