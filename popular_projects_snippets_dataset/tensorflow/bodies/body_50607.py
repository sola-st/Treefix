# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
# pylint: disable=line-too-long
"""Outputs a `Summary` protocol buffer with audio.

  The summary has up to `max_outputs` summary values containing audio. The
  audio is built from `tensor` which must be 3-D with shape `[batch_size,
  frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
  assumed to be in the range of `[-1.0, 1.0]` with a sample rate of
  `sample_rate`.

  The `tag` in the outputted Summary.Value protobufs is generated based on the
  name, with a suffix depending on the max_outputs setting:

  *  If `max_outputs` is 1, the summary value tag is '*name*/audio'.
  *  If `max_outputs` is greater than 1, the summary value tags are
     generated sequentially as '*name*/audio/0', '*name*/audio/1', etc

  Args:
    name: A name for the generated node. Will also serve as a series name in
      TensorBoard.
    tensor: A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
      or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
    sample_rate: A Scalar `float32` `Tensor` indicating the sample rate of the
      signal in hertz.
    max_outputs: Max number of batch elements to generate audio for.
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
  `tf.summary.audio`, and the return value will be an empty bytestring tensor,
  to avoid duplicate summary writing. This forwarding is best-effort and not all
  arguments will be preserved. Additionally:

  * The TF2 op just outputs the data under a single tag that contains multiple
    samples, rather than multiple tags (i.e. no "/0" or "/1" suffixes).

  To migrate to TF2, please use `tf.summary.audio` instead. Please check
  [Migrating tf.summary usage to
  TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x) for concrete
  steps for migration.

  #### How to Map Arguments

  | TF1 Arg Name  | TF2 Arg Name    | Note                                   |
  | :------------ | :-------------- | :------------------------------------- |
  | `name`        | `name`          | -                                      |
  | `tensor`      | `data`          | Input for this argument now must be    |
  :               :                 : three-dimensional `[k, t, c]`, where   :
  :               :                 : `k` is the number of audio clips, `t`  :
  :               :                 : is the number of frames, and `c` is    :
  :               :                 : the number of channels. Two-dimensional:
  :               :                 : input is no longer supported.          :
  | `sample_rate` | `sample_rate`   | -                                      |
  | -             | `step`          | Explicit int64-castable monotonic step |
  :               :                 : value. If omitted, this defaults to    :
  :               :                 : `tf.summary.experimental.get_step()`.  :
  | `max_outputs` | `max_outputs`   | -                                      |
  | `collections` | Not Supported   | -                                      |
  | `family`      | Removed         | Please use `tf.name_scope` instead to  |
  :               :                 : manage summary name prefix.            :
  | -             | `encoding`      | Optional constant str for the desired  |
  :               :                 : encoding. Check the docs for           :
  :               :                 : `tf.summary.audio` for latest supported:
  :               :                 : audio formats.                         :
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
    from tensorboard.summary.v2 import audio as audio_v2  # pylint: disable=g-import-not-at-top
    if tensor.shape.rank == 2:
        # TF2 op requires 3-D tensor, add the `channels` dimension.
        tensor = _array_ops.expand_dims_v2(tensor, axis=2)
    with _compat_summary_scope(name, family) as tag:
        audio_v2(
            name=tag,
            data=tensor,
            sample_rate=sample_rate,
            step=_get_step_for_v2(),
            max_outputs=max_outputs,
        )
    # Return an empty Tensor, which will be acceptable as an input to the
    # `tf.compat.v1.summary.merge()` API.
    exit(_constant_op.constant(b''))

# Fall back to legacy v1 audio implementation.
with _summary_op_util.summary_scope(
    name, family=family, values=[tensor]) as (tag, scope):
    sample_rate = _ops.convert_to_tensor(
        sample_rate, dtype=_dtypes.float32, name='sample_rate')
    val = _gen_logging_ops.audio_summary_v2(
        tag=tag, tensor=tensor, max_outputs=max_outputs,
        sample_rate=sample_rate, name=scope)
    _summary_op_util.collect(val, collections, [_ops.GraphKeys.SUMMARIES])
exit(val)
