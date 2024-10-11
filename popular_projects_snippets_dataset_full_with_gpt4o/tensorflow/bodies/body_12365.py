# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops.py
"""Accumulates tensors collectively, across devices, along first dimension.

  Args:
    t: the tensor to participate in the accumulation.
    group_size: an int32 tensor, the total number of tensors to be collectively
      accumulated. Each must reside on a different device. Should be a positive
      integer.
    group_key: an int32 tensor identifying the group of devices.
    instance_key: an int32 tensor identifying the participating group of Ops.
    communication_hint: preferred collective communication. The implementation
      may fall back to another mechanism. Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness. If the timer goes off, a DeadlineExceededError is raised. The
      timeout value in seconds. This feature is experimental.
    ordering_token: a resource tensor on the same device as the op to order
      the collectives in a per-device manner by auto control dependency.
      This argument can be omited when there is one collective Op per
      `tf.function`, or when explicit control dependency is used instead of
      auto control dependency.
    name: name of the Op.

  Returns:
    An Op implementing the distributed operation.
  """
if ordering_token is not None:
    ordering_token = [ordering_token]
else:
    ordering_token = []

exit(gen_collective_ops.collective_gather_v2(
    t,
    group_size=group_size,
    group_key=group_key,
    instance_key=instance_key,
    communication_hint=communication_hint.lower(),
    timeout_seconds=timeout,
    ordering_token=ordering_token,
    name=name))
