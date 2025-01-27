# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Resets the generator by a new state.

    See `__init__` for the meaning of "state".

    Args:
      state: the new state.
    """
state = _convert_to_state_tensor(state)
state.shape.assert_is_compatible_with([_get_state_size(self.algorithm)])
self._state_var.assign(state)
