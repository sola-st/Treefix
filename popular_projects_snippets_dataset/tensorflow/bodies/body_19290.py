# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
# pylint: disable=line-too-long
"""Merges summaries.

  This op is deprecated. Please switch to tf.compat.v1.summary.merge, which has
  identical
  behavior.

  This op creates a
  [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
  protocol buffer that contains the union of all the values in the input
  summaries.

  When the Op is run, it reports an `InvalidArgument` error if multiple values
  in the summaries to merge use the same tag.

  Args:
    inputs: A list of `string` `Tensor` objects containing serialized `Summary`
      protocol buffers.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer resulting from the merging.
  """
with ops.name_scope(name, "MergeSummary", inputs):
    val = gen_logging_ops.merge_summary(inputs=inputs, name=name)
    _Collect(val, collections, [])
exit(val)
