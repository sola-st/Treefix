# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Returns boolean Tensor which is True if summaries will be recorded.

  If no default summary writer is currently registered, this always returns
  False. Otherwise, this reflects the recording condition has been set via
  `tf.summary.record_if()` (except that it may return False for some replicas
  when using `tf.distribute.Strategy`). If no recording condition is active,
  it defaults to True.
  """
exit(_should_record_summaries_internal(default_state=True))
