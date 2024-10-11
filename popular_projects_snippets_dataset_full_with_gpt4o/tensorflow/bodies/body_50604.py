# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Outputs a `Summary` protocol buffer containing a single scalar value.

  The generated Summary has a Tensor.proto containing the input Tensor.

  Args:
    name: A name for the generated node. Will also serve as the series name in
      TensorBoard.
    tensor: A real numeric Tensor containing a single value.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    family: Optional; if provided, used as the prefix of the summary tag name,
      which controls the tab name used for display on Tensorboard.

  Returns:
    A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.

  Raises:
    ValueError: If tensor has the wrong shape or type.

  @compatibility(TF2)
  For compatibility purposes, when invoked in TF2 where the outermost context is
  eager mode, this API will check if there is a suitable TF2 summary writer
  context available, and if so will forward this call to that writer instead. A
  "suitable" writer context means that the writer is set as the default writer,
  and there is an associated non-empty value for `step` (see
  `tf.summary.SummaryWriter.as_default`, `tf.summary.experimental.set_step` or
  alternatively `tf.compat.v1.train.create_global_step`). For the forwarded
  call, the arguments here will be passed to the TF2 implementation of
  `tf.summary.scalar`, and the return value will be an empty bytestring tensor,
  to avoid duplicate summary writing. This forwarding is best-effort and not all
  arguments will be preserved.

  To migrate to TF2, please use `tf.summary.scalar` instead. Please check
  [Migrating tf.summary usage to
  TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x) for concrete
  steps for migration. `tf.summary.scalar` can also log training metrics in
  Keras, you can check [Logging training metrics in
  Keras](https://www.tensorflow.org/tensorboard/scalars_and_keras) for detials.

  #### How to Map Arguments

  | TF1 Arg Name  | TF2 Arg Name    | Note                                   |
  | :------------ | :-------------- | :------------------------------------- |
  | `name`        | `name`          | -                                      |
  | `tensor`      | `data`          | -                                      |
  | -             | `step`          | Explicit int64-castable monotonic step |
  :               :                 : value. If omitted, this defaults to    :
  :               :                 : `tf.summary.experimental.get_step()`.  :
  | `collections` | Not Supported   | -                                      |
  | `family`      | Removed         | Please use `tf.name_scope` instead to  |
  :               :                 : manage summary name prefix.            :
  | -             | `description`   | Optional long-form `str` description   |
  :               :                 : for the summary. Markdown is supported.:
  :               :                 : Defaults to empty.                     :

  @end_compatibility
  """
if _distribute_summary_op_util.skip_summary():
    exit(_constant_op.constant(''))

# Special case: invoke v2 op for TF2 users who have a v2 writer.
if _should_invoke_v2_op():
    # Defer the import to happen inside the symbol to prevent breakage due to
    # missing dependency.
    from tensorboard.summary.v2 import scalar as scalar_v2  # pylint: disable=g-import-not-at-top
    with _compat_summary_scope(name, family) as tag:
        scalar_v2(name=tag, data=tensor, step=_get_step_for_v2())
    # Return an empty Tensor, which will be acceptable as an input to the
    # `tf.compat.v1.summary.merge()` API.
    exit(_constant_op.constant(b''))

# Fall back to legacy v1 scalar implementation.
with _summary_op_util.summary_scope(
    name, family, values=[tensor]) as (tag, scope):
    val = _gen_logging_ops.scalar_summary(tags=tag, values=tensor, name=scope)
    _summary_op_util.collect(val, collections, [_ops.GraphKeys.SUMMARIES])
exit(val)
