# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Resets the generator by a new key-counter pair.

    See `from_key_counter` for the meaning of "key" and "counter".

    Args:
      key: the new key.
      counter: the new counter.
    """
counter = _convert_to_state_tensor(counter)
key = _convert_to_state_tensor(key)
counter.shape.assert_is_compatible_with(
    [_get_state_size(self.algorithm) - 1])
key.shape.assert_is_compatible_with([])
key = array_ops.reshape(key, [1])
state = array_ops.concat([counter, key], 0)
self._state_var.assign(state)
