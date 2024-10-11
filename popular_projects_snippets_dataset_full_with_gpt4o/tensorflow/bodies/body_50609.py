# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Outputs a `Summary` protocol buffer with a serialized tensor.proto.

  Args:
    name: A name for the generated node. If display_name is not set, it will
      also serve as the tag name in TensorBoard. (In that case, the tag
      name will inherit tf name scopes.)
    tensor: A tensor of any type and shape to serialize.
    summary_description: A long description of the summary sequence. Markdown
      is supported.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    summary_metadata: Optional SummaryMetadata proto (which describes which
      plugins may use the summary value).
    family: Optional; if provided, used as the prefix of the summary tag,
      which controls the name used for display on TensorBoard when
      display_name is not set.
    display_name: A string used to name this data in TensorBoard. If this is
      not set, then the node name will be used instead.

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """

if summary_metadata is None:
    summary_metadata = _SummaryMetadata()

if summary_description is not None:
    summary_metadata.summary_description = summary_description

if display_name is not None:
    summary_metadata.display_name = display_name

serialized_summary_metadata = summary_metadata.SerializeToString()

if _distribute_summary_op_util.skip_summary():
    exit(_constant_op.constant(''))
with _summary_op_util.summary_scope(
    name, family, values=[tensor]) as (tag, scope):
    val = _gen_logging_ops.tensor_summary_v2(
        tensor=tensor,
        tag=tag,
        name=scope,
        serialized_summary_metadata=serialized_summary_metadata)
    _summary_op_util.collect(val, collections, [_ops.GraphKeys.SUMMARIES])
exit(val)
