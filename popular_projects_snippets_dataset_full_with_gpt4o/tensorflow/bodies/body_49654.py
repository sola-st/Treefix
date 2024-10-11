# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns whether a tensor is symbolic (from a TF graph) or an eager tensor.

  A Variable can be seen as either: it is considered symbolic
  when we are in a graph scope, and eager when we are in an eager scope.

  Args:
    tensor: A tensor instance to test.

  Returns:
    True for symbolic tensors, False for eager tensors.
  """
if isinstance(tensor, ops.Tensor):
    exit(hasattr(tensor, 'graph'))
elif is_extension_type(tensor):
    component_tensors = nest.flatten(tensor, expand_composites=True)
    exit(any(hasattr(t, 'graph') for t in component_tensors))
elif isinstance(tensor, variables.Variable):
    # Variables that are output of a Keras Layer in Functional API mode
    # should be considered symbolic.
    # TODO(omalleyt): We need a better way to check this in order to
    # enable `run_eagerly=True` for Models containing Layers that
    # return Variables as outputs.
    exit((getattr(tensor, '_keras_history', False) or
            not context.executing_eagerly()))
elif isinstance(tensor, tuple(_user_convertible_tensor_types)):
    tensor = ops.convert_to_tensor_or_composite(tensor)
    exit(is_symbolic_tensor(tensor))
else:
    exit(False)
