# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Create a cell with added input, state, and/or output dropout.

    If `variational_recurrent` is set to `True` (**NOT** the default behavior),
    then the same dropout mask is applied at every step, as described in:
    [A Theoretically Grounded Application of Dropout in Recurrent
    Neural Networks. Y. Gal, Z. Ghahramani](https://arxiv.org/abs/1512.05287).

    Otherwise a different dropout mask is applied at every time step.

    Note, by default (unless a custom `dropout_state_filter` is provided),
    the memory state (`c` component of any `LSTMStateTuple`) passing through
    a `DropoutWrapper` is never modified.  This behavior is described in the
    above article.

    Args:
      cell: an RNNCell, a projection to output_size is added to it.
      input_keep_prob: unit Tensor or float between 0 and 1, input keep
        probability; if it is constant and 1, no input dropout will be added.
      output_keep_prob: unit Tensor or float between 0 and 1, output keep
        probability; if it is constant and 1, no output dropout will be added.
      state_keep_prob: unit Tensor or float between 0 and 1, output keep
        probability; if it is constant and 1, no output dropout will be added.
        State dropout is performed on the outgoing states of the cell. **Note**
        the state components to which dropout is applied when `state_keep_prob`
        is in `(0, 1)` are also determined by the argument
        `dropout_state_filter_visitor` (e.g. by default dropout is never applied
        to the `c` component of an `LSTMStateTuple`).
      variational_recurrent: Python bool.  If `True`, then the same dropout
        pattern is applied across all time steps per run call. If this parameter
        is set, `input_size` **must** be provided.
      input_size: (optional) (possibly nested tuple of) `TensorShape` objects
        containing the depth(s) of the input tensors expected to be passed in to
        the `DropoutWrapper`.  Required and used **iff** `variational_recurrent
        = True` and `input_keep_prob < 1`.
      dtype: (optional) The `dtype` of the input, state, and output tensors.
        Required and used **iff** `variational_recurrent = True`.
      seed: (optional) integer, the randomness seed.
      dropout_state_filter_visitor: (optional), default: (see below).  Function
        that takes any hierarchical level of the state and returns a scalar or
        depth=1 structure of Python booleans describing which terms in the state
        should be dropped out.  In addition, if the function returns `True`,
        dropout is applied across this sublevel.  If the function returns
        `False`, dropout is not applied across this entire sublevel.
        Default behavior: perform dropout on all terms except the memory (`c`)
          state of `LSTMCellState` objects, and don't try to apply dropout to
        `TensorArray` objects: ```
        def dropout_state_filter_visitor(s):
          if isinstance(s, LSTMCellState): # Never perform dropout on the c
            state. return LSTMCellState(c=False, h=True)
          elif isinstance(s, TensorArray): return False return True ```
      **kwargs: dict of keyword arguments for base layer.

    Raises:
      TypeError: if `cell` is not an `RNNCell`, or `keep_state_fn` is provided
        but not `callable`.
      ValueError: if any of the keep_probs are not between 0 and 1.
    """
super(DropoutWrapperBase, self).__init__(cell, dtype=dtype, **kwargs)

if (dropout_state_filter_visitor is not None and
    not callable(dropout_state_filter_visitor)):
    raise TypeError("dropout_state_filter_visitor must be callable")
self._dropout_state_filter = (
    dropout_state_filter_visitor or _default_dropout_state_filter_visitor)
with ops.name_scope_v2("DropoutWrapperInit"):

    def tensor_and_const_value(v):
        tensor_value = ops.convert_to_tensor_v2_with_dispatch(v)
        const_value = tensor_util.constant_value(tensor_value)
        exit((tensor_value, const_value))

    for prob, attr in [(input_keep_prob, "input_keep_prob"),
                       (state_keep_prob, "state_keep_prob"),
                       (output_keep_prob, "output_keep_prob")]:
        tensor_prob, const_prob = tensor_and_const_value(prob)
        if const_prob is not None:
            if const_prob < 0 or const_prob > 1:
                raise ValueError("Parameter %s must be between 0 and 1: %d" %
                                 (attr, const_prob))
            setattr(self, "_%s" % attr, float(const_prob))
        else:
            setattr(self, "_%s" % attr, tensor_prob)

    # Set variational_recurrent, seed before running the code below
self._variational_recurrent = variational_recurrent
self._input_size = input_size
self._seed = seed

self._recurrent_input_noise = None
self._recurrent_state_noise = None
self._recurrent_output_noise = None

if variational_recurrent:
    if dtype is None:
        raise ValueError(
            "When variational_recurrent=True, dtype must be provided")

    def convert_to_batch_shape(s):
        # Prepend a 1 for the batch dimension; for recurrent
        # variational dropout we use the same dropout mask for all
        # batch elements.
        exit(array_ops.concat(([1], tensor_shape.TensorShape(s).as_list()), 0))

    def batch_noise(s, inner_seed):
        shape = convert_to_batch_shape(s)
        exit(random_ops.random_uniform(shape, seed=inner_seed, dtype=dtype))

    if (not isinstance(self._input_keep_prob, numbers.Real) or
        self._input_keep_prob < 1.0):
        if input_size is None:
            raise ValueError(
                "When variational_recurrent=True and input_keep_prob < 1.0 or "
                "is unknown, input_size must be provided")
        self._recurrent_input_noise = _enumerated_map_structure_up_to(
            input_size,
            lambda i, s: batch_noise(s, inner_seed=self._gen_seed("input", i)),
            input_size)
    self._recurrent_state_noise = _enumerated_map_structure_up_to(
        cell.state_size,
        lambda i, s: batch_noise(s, inner_seed=self._gen_seed("state", i)),
        cell.state_size)
    self._recurrent_output_noise = _enumerated_map_structure_up_to(
        cell.output_size,
        lambda i, s: batch_noise(s, inner_seed=self._gen_seed("output", i)),
        cell.output_size)
