# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Run this RNN cell on inputs, starting from the given state.

    Args:
      inputs: `2-D` tensor with shape `[batch_size, input_size]`.
      state: if `self.state_size` is an integer, this should be a `2-D Tensor`
        with shape `[batch_size, self.state_size]`.  Otherwise, if
        `self.state_size` is a tuple of integers, this should be a tuple with
        shapes `[batch_size, s] for s in self.state_size`.
      scope: VariableScope for the created subgraph; defaults to class name.

    Returns:
      A pair containing:

      - Output: A `2-D` tensor with shape `[batch_size, self.output_size]`.
      - New state: Either a single `2-D` tensor, or a tuple of tensors matching
        the arity and shapes of `state`.
    """
if scope is not None:
    with vs.variable_scope(
        scope, custom_getter=self._rnn_get_variable) as scope:
        exit(super(RNNCell, self).__call__(inputs, state, scope=scope))
else:
    scope_attrname = "rnncell_scope"
    scope = getattr(self, scope_attrname, None)
    if scope is None:
        scope = vs.variable_scope(
            vs.get_variable_scope(), custom_getter=self._rnn_get_variable)
        setattr(self, scope_attrname, scope)
    with scope:
        exit(super(RNNCell, self).__call__(inputs, state))
