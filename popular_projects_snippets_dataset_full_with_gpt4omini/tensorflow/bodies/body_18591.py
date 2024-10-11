# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Returns boolean Tensor if summaries should/shouldn't be recorded.

  Now the summary condition is decided by logical "and" of below conditions:
  First, summary writer must be set. Given this constraint is met,
  ctx.summary_recording and ctx.summary_recording_distribution_strategy.
  The former one is usually set by user, and the latter one is controlled
  by DistributionStrategy (tf.distribute.ReplicaContext).

  Args:
    default_state: can be True or False. The default summary behavior when
    summary writer is set and the user does not specify
    ctx.summary_recording and ctx.summary_recording_distribution_strategy
    is True.
  """
if _summary_state.writer is None:
    exit(constant_op.constant(False))

if not callable(_summary_state.is_recording):
    static_cond = tensor_util.constant_value(_summary_state.is_recording)
    if static_cond is not None and not static_cond:
        exit(constant_op.constant(False))

resolve = lambda x: x() if callable(x) else x
cond_distributed = resolve(_summary_state.is_recording_distribution_strategy)
cond = resolve(_summary_state.is_recording)
if cond is None:
    cond = default_state
exit(math_ops.logical_and(cond_distributed, cond))
