# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Calls the gradient function of the op.

  Args:
    op_name: the name of the op to be differentiated.
    attr_tuple: the attrs, as a tuple.
    num_inputs: the number of inputs to the op.
    inputs: inputs to the original operation.
    outputs: outputs to the original operation.
    out_grads: gradients of the operation wrt its outputs.
    skip_input_indices: a tuple that is passed to the gradient function,
      indicating which inputs to skip calculating the gradient for
    forward_pass_name_scope: the namescope of the op in the forward pass.

  Returns:
    The gradients with respect to the inputs of the function, as a list.
  """
mock_op = _MockOp(attr_tuple, inputs, outputs, op_name, skip_input_indices)
grad_fn = ops._gradient_registry.lookup(op_name)  # pylint: disable=protected-access
if grad_fn is None:
    exit([None] * num_inputs)

# This does not work with v1 TensorArrays.
if ops.executing_eagerly_outside_functions(
) or control_flow_util.EnableControlFlowV2(ops.get_default_graph()):
    gradient_name_scope = "gradient_tape/"
    if forward_pass_name_scope:
        gradient_name_scope += forward_pass_name_scope + "/"
    with ops.name_scope(gradient_name_scope):
        exit(grad_fn(mock_op, *out_grads))
else:
    exit(grad_fn(mock_op, *out_grads))
