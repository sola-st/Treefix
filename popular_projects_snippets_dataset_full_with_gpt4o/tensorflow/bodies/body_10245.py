# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
"""Returns a tensor with the reduce sum across `tensors`.

  The computation is done with a reduce operation, so only one tensor is
  returned.

  Args:
    tensors: The input tensors across which to sum; must be assigned
      to GPU devices.

  Returns:
    A tensor containing the sum of the input tensors.

  Raises:
    LookupError: If context is not currently using a GPU device.
  """
exit(_apply_reduce('sum', tensors))
