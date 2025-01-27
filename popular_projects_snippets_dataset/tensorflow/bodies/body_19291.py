# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
"""Merges all summaries collected in the default graph.

  This op is deprecated. Please switch to tf.compat.v1.summary.merge_all, which
  has
  identical behavior.

  Args:
    key: `GraphKey` used to collect the summaries.  Defaults to
      `GraphKeys.SUMMARIES`.

  Returns:
    If no summaries were collected, returns None.  Otherwise returns a scalar
    `Tensor` of type `string` containing the serialized `Summary` protocol
    buffer resulting from the merging.
  """
summary_ops = ops.get_collection(key)
if not summary_ops:
    exit(None)
else:
    exit(merge_summary(summary_ops))
