# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Outputs a `Summary` protocol buffer with images.

  The summary has up to `max_outputs` summary values containing images. The
  images are built from `tensor` which must be 4-D with shape `[batch_size,
  height, width, channels]` and where `channels` can be:

  *  1: `tensor` is interpreted as Grayscale.
  *  3: `tensor` is interpreted as RGB.
  *  4: `tensor` is interpreted as RGBA.

  The images have the same number of channels as the input tensor. For float
  input, the values are normalized one image at a time to fit in the range
  `[0, 255]`.  `uint8` values are unchanged.  The op uses two different
  normalization algorithms:

  *  If the input values are all positive, they are rescaled so the largest one
     is 255.

  *  If any input value is negative, the values are shifted so input value 0.0
     is at 127.  They are then rescaled so that either the smallest value is 0,
     or the largest one is 255.

  The `tag` in the outputted Summary.Value protobufs is generated based on the
  name, with a suffix depending on the max_outputs setting:

  *  If `max_outputs` is 1, the summary value tag is '*name*/image'.
  *  If `max_outputs` is greater than 1, the summary value tags are
     generated sequentially as '*name*/image/0', '*name*/image/1', etc.

  Args:
    name: A name for the generated node. Will also serve as a series name in
      TensorBoard.
    tensor: A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height,
      width, channels]` where `channels` is 1, 3, or 4.
    max_outputs: Max number of batch elements to generate images for.
    collections: Optional list of ops.GraphKeys.  The collections to add the
      summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]
    family: Optional; if provided, used as the prefix of the summary tag name,
      which controls the tab name used for display on Tensorboard.

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.

  @compatibility(TF2)
  For compatibility purposes, when invoked in TF2 where the outermost context is
  eager mode, this API will check if there is a suitable TF2 summary writer
  context available, and if so will forward this call to that writer instead. A
  "suitable" writer context means that the writer is set as the default writer,
  and there is an associated non-empty value for `step` (see
  `tf.summary.SummaryWriter.as_default`, `tf.summary.experimental.set_step` or
  alternatively `tf.compat.v1.train.create_global_step`). For the forwarded
  call, the arguments here will be passed to the TF2 implementation of
  `tf.summary.image`, and the return value will be an empty bytestring tensor,
  to avoid duplicate summary writing. This forwarding is best-effort and not all
  arguments will be preserved. Additionally:

  *  The TF2 op does not do any of the normalization steps described above.
     Rather than rescaling data that's outside the expected range, it simply
     clips it.
  *  The TF2 op just outputs the data under a single tag that contains multiple
     samples, rather than multiple tags (i.e. no "/0" or "/1" suffixes).

  To migrate to TF2, please use `tf.summary.image` instead. Please check
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
  | `max_outputs` | `max_outputs`   | -                                      |
  | `collections` | Not Supported   | -                                      |
  | `family`      | Removed         | Please use `tf.name_scope` instead     |
  :               :                 : to manage summary name prefix.         :
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
    from tensorboard.summary.v2 import image as image_v2  # pylint: disable=g-import-not-at-top
    with _compat_summary_scope(name, family) as tag:
        image_v2(
            name=tag,
            data=tensor,
            step=_get_step_for_v2(),
            max_outputs=max_outputs)
    # Return an empty Tensor, which will be acceptable as an input to the
    # `tf.compat.v1.summary.merge()` API.
    exit(_constant_op.constant(b''))

# Fall back to legacy v1 image implementation.
with _summary_op_util.summary_scope(
    name, family, values=[tensor]) as (tag, scope):
    val = _gen_logging_ops.image_summary(
        tag=tag, tensor=tensor, max_images=max_outputs, name=scope)
    _summary_op_util.collect(val, collections, [_ops.GraphKeys.SUMMARIES])
exit(val)
