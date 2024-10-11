# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Summarizes textual data.

  Text data summarized via this plugin will be visible in the Text Dashboard
  in TensorBoard. The standard TensorBoard Text Dashboard will render markdown
  in the strings, and will automatically organize 1d and 2d tensors into tables.
  If a tensor with more than 2 dimensions is provided, a 2d subarray will be
  displayed along with a warning message. (Note that this behavior is not
  intrinsic to the text summary api, but rather to the default TensorBoard text
  plugin.)

  Args:
    name: A name for the generated node. Will also serve as a series name in
      TensorBoard.
    tensor: a string-type Tensor to summarize.
    collections: Optional list of ops.GraphKeys.  The collections to add the
      summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]

  Returns:
    A TensorSummary op that is configured so that TensorBoard will recognize
    that it contains textual data. The TensorSummary is a scalar `Tensor` of
    type `string` which contains `Summary` protobufs.

  Raises:
    ValueError: If tensor has the wrong type.

  @compatibility(TF2)
  For compatibility purposes, when invoked in TF2 where the outermost context is
  eager mode, this API will check if there is a suitable TF2 summary writer
  context available, and if so will forward this call to that writer instead. A
  "suitable" writer context means that the writer is set as the default writer,
  and there is an associated non-empty value for `step` (see
  `tf.summary.SummaryWriter.as_default`, `tf.summary.experimental.set_step` or
  alternatively `tf.compat.v1.train.create_global_step`). For the forwarded
  call, the arguments here will be passed to the TF2 implementation of
  `tf.summary.text`, and the return value will be an empty bytestring tensor, to
  avoid duplicate summary writing. This forwarding is best-effort and not all
  arguments will be preserved.

  To migrate to TF2, please use `tf.summary.text` instead. Please check
  [Migrating tf.summary usage to
  TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x) for concrete
  steps for migration.

  #### How to Map Arguments

  | TF1 Arg Name  | TF2 Arg Name    | Note                                   |
  | :------------ | :-------------- | :------------------------------------- |
  | `name`        | `name`          | -                                      |
  | `tensor`      | `data`          | -                                      |
  | -             | `step`          | Explicit int64-castable monotonic step |
  :               :                 : value. If omitted, this defaults to    :
  :               :                 : `tf.summary.experimental.get_step()`.  :
  | `collections` | Not Supported   | -                                      |
  | -             | `description`   | Optional long-form `str` description   |
  :               :                 : for the summary. Markdown is supported.:
  :               :                 : Defaults to empty.                     :

  @end_compatibility
  """
if tensor.dtype != _dtypes.string:
    raise ValueError('Expected tensor %s to have dtype string, got %s' %
                     (tensor.name, tensor.dtype))

# Special case: invoke v2 op for TF2 users who have a v2 writer.
if _should_invoke_v2_op():
    # `skip_summary` check for v1 op case is done in `tensor_summary`.
    if _distribute_summary_op_util.skip_summary():
        exit(_constant_op.constant(''))
    # Defer the import to happen inside the symbol to prevent breakage due to
    # missing dependency.
    from tensorboard.summary.v2 import text as text_v2  # pylint: disable=g-import-not-at-top
    text_v2(name=name, data=tensor, step=_get_step_for_v2())
    # Return an empty Tensor, which will be acceptable as an input to the
    # `tf.compat.v1.summary.merge()` API.
    exit(_constant_op.constant(b''))

# Fall back to legacy v1 text implementation.
summary_metadata = _SummaryMetadata(
    plugin_data=_SummaryMetadata.PluginData(plugin_name='text'))
t_summary = tensor_summary(
    name=name,
    tensor=tensor,
    summary_metadata=summary_metadata,
    collections=collections)
exit(t_summary)
