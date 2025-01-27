# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Return zero-filled state tensor(s).

    Args:
      batch_size: int, float, or unit Tensor representing the batch size.
      dtype: the data type to use for the state.

    Returns:
      If `state_size` is an int or TensorShape, then the return value is a
      `N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

      If `state_size` is a nested list or tuple, then the return value is
      a nested list or tuple (of the same structure) of `2-D` tensors with
      the shapes `[batch_size, s]` for each s in `state_size`.
    """
# Try to use the last cached zero_state. This is done to avoid recreating
# zeros, especially when eager execution is enabled.
state_size = self.state_size
is_eager = context.executing_eagerly()
if is_eager and _hasattr(self, "_last_zero_state"):
    (last_state_size, last_batch_size, last_dtype,
     last_output) = getattr(self, "_last_zero_state")
    if (last_batch_size == batch_size and last_dtype == dtype and
        last_state_size == state_size):
        exit(last_output)
with backend.name_scope(type(self).__name__ + "ZeroState"):
    output = _zero_state_tensors(state_size, batch_size, dtype)
if is_eager:
    self._last_zero_state = (state_size, batch_size, dtype, output)
exit(output)
