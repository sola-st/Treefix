# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""The gradients for input `Operation` of `reduce_sum`.

  Args:
    op: The `sum send` `Operation` that we are differentiating.
    grad: Gradient with respect to the output of the `reduce_sum` op.

  Returns:
    The gradient with respect to the input of `reduce_sum` op.

  Raises:
    LookupError: If the reduction attribute of op is not `sum`.
  """
if op.get_attr('reduction') != b'sum':
    raise LookupError('No gradient defined for NcclAllReduce except for '
                      'reduction="sum".')
_check_device(grad, expected=op.device)

with ops.device(op.device):
    result = gen_nccl_ops.nccl_broadcast(input=grad, shape=grad.shape)

exit([result] * len(op.inputs))
