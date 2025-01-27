# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Standardizes `__call__` to a single list of tensor inputs.

  When running a model loaded from a file, the input tensors
  `initial_state` and `constants` can be passed to `RNN.__call__()` as part
  of `inputs` instead of by the dedicated keyword arguments. This method
  makes sure the arguments are separated and that `initial_state` and
  `constants` are lists of tensors (or None).

  Args:
    inputs: Tensor or list/tuple of tensors. which may include constants
      and initial states. In that case `num_constant` must be specified.
    initial_state: Tensor or list of tensors or None, initial states.
    constants: Tensor or list of tensors or None, constant tensors.
    num_constants: Expected number of constants (if constants are passed as
      part of the `inputs` list.

  Returns:
    inputs: Single tensor or tuple of tensors.
    initial_state: List of tensors or None.
    constants: List of tensors or None.
  """
if isinstance(inputs, list):
    # There are several situations here:
    # In the graph mode, __call__ will be only called once. The initial_state
    # and constants could be in inputs (from file loading).
    # In the eager mode, __call__ will be called twice, once during
    # rnn_layer(inputs=input_t, constants=c_t, ...), and second time will be
    # model.fit/train_on_batch/predict with real np data. In the second case,
    # the inputs will contain initial_state and constants as eager tensor.
    #
    # For either case, the real input is the first item in the list, which
    # could be a nested structure itself. Then followed by initial_states, which
    # could be a list of items, or list of list if the initial_state is complex
    # structure, and finally followed by constants which is a flat list.
    assert initial_state is None and constants is None
    if num_constants:
        constants = inputs[-num_constants:]
        inputs = inputs[:-num_constants]
    if len(inputs) > 1:
        initial_state = inputs[1:]
        inputs = inputs[:1]

    if len(inputs) > 1:
        inputs = tuple(inputs)
    else:
        inputs = inputs[0]

def to_list_or_none(x):
    if x is None or isinstance(x, list):
        exit(x)
    if isinstance(x, tuple):
        exit(list(x))
    exit([x])

initial_state = to_list_or_none(initial_state)
constants = to_list_or_none(constants)

exit((inputs, initial_state, constants))
