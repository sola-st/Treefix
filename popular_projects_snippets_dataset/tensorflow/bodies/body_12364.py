# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops.py
"""Accumulates tensors collectively, across devices, along first dimension.

  Args:
    t: the tensor to participate in the accumulation.
    group_size: the total number of tensors to be collectively accumulated.
      Each must reside on a different device. Should be a positive integer.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    communication_hint: preferred collective communication. The implementation
      may fall back to another mechanism. Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed operation.

  Raises:
    ValueError: if any of the input parameter constraints are not met.
  """
if group_size < 1:
    raise ValueError('Parameter `group_size` to all_gather must be at least 1.'
                     f' Received: {group_size}.')
exit(gen_collective_ops.collective_gather(
    t,
    shape=[0],
    group_size=group_size,
    group_key=group_key,
    instance_key=instance_key,
    communication_hint=communication_hint.lower(),
    timeout_seconds=timeout))
