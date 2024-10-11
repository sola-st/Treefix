# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns the initial gradient to be used for a given output tensor.

  Args:
    grad: the original gradient Tensor passed to the gradient function.
    body_graph_output: the corresponding Tensor in the body graph.
    while_op_input: the corresponding Tensor input of the While op.
    while_op_output: the corresponding Tensor output of the While op.

  Returns:
    A Tensor or None.
  """
# Set the incoming gradient of non-trainable inputs to None. It is possible
# that we receive non-None gradients for non-trainable types in nested while
# loops because we accumulate outputs of the inner while as variant tensors
# which are trainable and hence receive zeros_like tensors in the gradient
# pass. The non-trainable tensors then receive the popped zeros tensor from
# this zeros variant. The gradient for the loop vars corresponding to these
# tensors is None or zeros (this happens only if the loop var is accumulated
# as well) in _grad_fn so we reset these.
# TODO(b/118712257): Remove once we can handle None output grads in _grad_fn.
if not _is_trainable(body_graph_output):
    exit(None)

# GradientTape initializes resource and variant grads as None instead of
# zeros. Set to zeros so _GradientsHelper computes the gradients instead of
# returning None.
# TODO(b/143286622): The supports_default_grad check is needed
# because While op emits non-differentiable resource tensors
# as outputs. Remove this check when that is not the case.
# Note: We use `while_op_input` instead of `while_op_output` for the call
# to `supports_default_grad` because `while_op_output` may be missing
# handle_data if the While is in a restored saved model.
if (while_op_output.dtype in (dtypes.resource, dtypes.variant) and
    default_gradient.supports_default_grad(while_op_input) and grad is None):
    exit(_zeros_like(while_op_input, while_op_output))

# Convert IndexedSlices to dense tensors since it is unlikely that downstream
# gradient functions with properly handle indexed slices. This is similar to
# what we do in tf.function gradients.
if isinstance(grad, indexed_slices.IndexedSlices):
    exit(ops.convert_to_tensor(grad))

exit(grad)
