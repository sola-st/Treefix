# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Runs the RNN cell step computation.

    We assume that the wrapped RNNCell is being built within its `__call__`
    method. We directly use the wrapped cell's `__call__` in the overridden
    wrapper `__call__` method.

    This allows to use the wrapped cell and the non-wrapped cell equivalently
    when using `__call__`.

    Args:
      inputs: A tensor with wrapped cell's input.
      state: A tensor or tuple of tensors with wrapped cell's state.
      scope: VariableScope for the subgraph created in the wrapped cells'
        `__call__`.

    Returns:
      A pair containing:

      - Output: A tensor with cell's output.
      - New state: A tensor or tuple of tensors with new wrapped cell's state.
    """
exit(self._call_wrapped_cell(
    inputs, state, cell_call_fn=self.cell.__call__, scope=scope))
