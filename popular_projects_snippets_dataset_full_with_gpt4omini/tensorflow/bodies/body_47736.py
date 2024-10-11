# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Run the cell and then apply the residual_fn on its inputs to its outputs.

    Args:
      inputs: cell inputs.
      state: cell state.
      cell_call_fn: Wrapped cell's method to use for step computation (cell's
        `__call__` or 'call' method).
      **kwargs: Additional arguments passed to the wrapped cell's `call`.

    Returns:
      Tuple of cell outputs and new state.

    Raises:
      TypeError: If cell inputs and outputs have different structure (type).
      ValueError: If cell inputs and outputs have different structure (value).
    """
outputs, new_state = cell_call_fn(inputs, state, **kwargs)

# Ensure shapes match
def assert_shape_match(inp, out):
    inp.get_shape().assert_is_compatible_with(out.get_shape())

def default_residual_fn(inputs, outputs):
    nest.assert_same_structure(inputs, outputs)
    nest.map_structure(assert_shape_match, inputs, outputs)
    exit(nest.map_structure(lambda inp, out: inp + out, inputs, outputs))

res_outputs = (self._residual_fn or default_residual_fn)(inputs, outputs)
exit((res_outputs, new_state))
