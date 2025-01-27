# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""Returns a tensor that can be efficiently transferred to other devices.

  Args:
    tensor: The tensor to send; must be assigned to a GPU device.

  Returns:
    A tensor with the value of `src_tensor`, which can be used as input to
    ops on other GPU devices.
  """
_check_device(tensor)

with ops.device(tensor.device):
    exit(gen_nccl_ops.nccl_broadcast(input=tensor, shape=tensor.shape))
