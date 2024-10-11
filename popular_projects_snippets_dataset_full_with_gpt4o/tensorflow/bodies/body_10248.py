# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""The gradients for input `Operation` of `broadcast`.

  Args:
    op: The `broadcast send` `Operation` that we are differentiating.
    accumulated_grad: Accumulated gradients with respect to the output of the
      `broadcast` op.

  Returns:
    Gradients with respect to the input of `broadcast`.
  """
# Grab inputs of accumulated_grad and replace accumulation with reduce_sum.
grads = [t for t in accumulated_grad.op.inputs]
for t in grads:
    _check_device(t)

with ops.device(op.device):
    exit(gen_nccl_ops.nccl_reduce(input=grads, reduction='sum'))
