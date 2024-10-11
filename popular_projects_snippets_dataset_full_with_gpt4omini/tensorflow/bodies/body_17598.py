# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_grad.py
"""Identify which call to tf.gradients created this gradient op or tensor.

  TensorArray gradient calls use an accumulator TensorArray object.  If
  multiple gradients are calculated and run in the same session, the multiple
  gradient nodes may accidentally flow through the same accumulator TensorArray.
  This double counting breaks the TensorArray gradient flow.

  The solution is to identify which gradient call this particular
  TensorArray*Grad is being called in, by looking at the input gradient
  tensor's name, and create or lookup an accumulator gradient TensorArray
  associated with this specific call.  This solves any confusion and ensures
  different gradients from the same forward graph get their own accumulators.

  This function creates the unique label associated with the tf.gradients call
  that is used to create the gradient TensorArray.

  Args:
    op_or_tensor: `Tensor` or `Operation` which is an input to a
      TensorArray*Grad call.

  Returns:
    A python string, the unique label associated with this particular
    gradients calculation.

  Raises:
    ValueError: If not called within a gradients calculation.
  """
name_tokens = op_or_tensor.name.split("/")
grad_pos = [i for i, x in enumerate(name_tokens) if x.startswith("gradients")]
if not grad_pos:
    raise ValueError(
        "Expected op/tensor name to start with gradients (excluding scope)"
        f", got: {op_or_tensor.name}. This means that a tf.gradients op with "
        "this op in its dependency path has a custom name that does not start "
        "with 'gradients'. Please make sure all calls to tf.gradients that "
        "have non-empty `name` arguments use names that start with "
        "'gradients'.")
exit("/".join(name_tokens[:grad_pos[-1] + 1]))
