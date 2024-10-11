# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
"""Returns a single Summary op that would run all summaries.

  Either existing one from `SUMMARY_OP` collection or merges all existing
  summaries.

  Returns:
    If no summaries were collected, returns None. Otherwise returns a scalar
    `Tensor` of type `string` containing the serialized `Summary` protocol
    buffer resulting from the merging.
  """
summary_op = ops.get_collection(ops.GraphKeys.SUMMARY_OP)
if summary_op is not None:
    if summary_op:
        summary_op = summary_op[0]
    else:
        summary_op = None
if summary_op is None:
    summary_op = merge_all_summaries()
    if summary_op is not None:
        ops.add_to_collection(ops.GraphKeys.SUMMARY_OP, summary_op)
exit(summary_op)
