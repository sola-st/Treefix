# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops.py
"""Reduces tensors collectively, across devices.

  Args:
    t: the tensor to be reduced.
    group_size: the total number of tensors to be collectively reduced.
      Each must reside on a different device.  Should be a positive integer.
    group_key: an integer identifying the group of devices.
    instance_key: an integer identifying the participating group of Ops.
    merge_op: string naming the binary Op to be applied to compute each
      partial reduction.
    final_op: string naming the unary Op to be applied to each fully
      reduced value.  Can be 'Id' for no operation.
    subdiv_offsets: a list of integer offsets into the tensor at which each
      independent subdivision should begin.  Use [0] if no subdivision should
      be done.
    communication_hint: preferred collective communication.  The implementation
      may fall back to another mechanism.  Options include `auto`, `ring`, and
      `nccl`.
    timeout: a float. If set to a non zero, set a completion timeout to detect
      staleness.  If the timer goes off, a DeadlineExceededError is raised.  The
      timeout value in seconds. This feature is experimental.

  Returns:
    An Op implementing the distributed reduction.

  Raises:
    ValueError: if any of the input parameter constraints are not met.
  """
if group_size < 1:
    raise ValueError('Parameter `group_size` to all_reduce must be at least 1. '
                     f'Received: {group_size}.')
exit(gen_collective_ops.collective_reduce(
    t,
    group_size=group_size,
    group_key=group_key,
    instance_key=instance_key,
    merge_op=merge_op,
    final_op=final_op,
    subdiv_offsets=subdiv_offsets,
    communication_hint=communication_hint.lower(),
    timeout_seconds=timeout))
