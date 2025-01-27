# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
# pylint: disable=line-too-long
"""Outputs a `Summary` protocol buffer with scalar values.

  This ops is deprecated. Please switch to tf.summary.scalar.
  For an explanation of why this op was deprecated, and information on how to
  migrate, look
  ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

  The input `tags` and `values` must have the same shape.  The generated
  summary has a summary value for each tag-value pair in `tags` and `values`.

  Args:
    tags: A `string` `Tensor`.  Tags for the summaries.
    values: A real numeric Tensor.  Values for the summaries.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """
with ops.name_scope(name, "ScalarSummary", [tags, values]) as scope:
    val = gen_logging_ops.scalar_summary(tags=tags, values=values, name=scope)
    _Collect(val, collections, [ops.GraphKeys.SUMMARIES])
exit(val)
