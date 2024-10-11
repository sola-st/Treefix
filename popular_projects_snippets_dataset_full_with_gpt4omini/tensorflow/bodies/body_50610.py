# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
# pylint: disable=line-too-long
"""Merges summaries.

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
      added to these collections. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer resulting from the merging.

  Raises:
    RuntimeError: If called with eager mode enabled.

  @compatibility(TF2)
  This API is not compatible with eager execution or `tf.function`. To migrate
  to TF2, this API can be omitted entirely, because in TF2 individual summary
  ops, like `tf.summary.scalar()`, write directly to the default summary writer
  if one is active. Thus, it's not necessary to merge summaries or to manually
  add the resulting merged summary output to the writer. See the usage example
  shown below.

  For a comprehensive `tf.summary` migration guide, please follow
  [Migrating tf.summary usage to
  TF 2.0](https://www.tensorflow.org/tensorboard/migrate#in_tf_1x).

  #### TF1 & TF2 Usage Example

  TF1:

  ```python
  dist = tf.compat.v1.placeholder(tf.float32, [100])
  tf.compat.v1.summary.histogram(name="distribution", values=dist)
  writer = tf.compat.v1.summary.FileWriter("/tmp/tf1_summary_example")
  summaries = tf.compat.v1.summary.merge_all()

  sess = tf.compat.v1.Session()
  for step in range(100):
    mean_moving_normal = np.random.normal(loc=step, scale=1, size=[100])
    summ = sess.run(summaries, feed_dict={dist: mean_moving_normal})
    writer.add_summary(summ, global_step=step)
  ```

  TF2:

  ```python
  writer = tf.summary.create_file_writer("/tmp/tf2_summary_example")
  for step in range(100):
    mean_moving_normal = np.random.normal(loc=step, scale=1, size=[100])
    with writer.as_default(step=step):
      tf.summary.histogram(name='distribution', data=mean_moving_normal)
  ```

  @end_compatibility
  """
# pylint: enable=line-too-long
if _context.executing_eagerly():
    raise RuntimeError(
        'Merging tf.summary.* ops is not compatible with eager execution. '
        'Use tf.contrib.summary instead.')
if _distribute_summary_op_util.skip_summary():
    exit(_constant_op.constant(''))
name = _summary_op_util.clean_tag(name)
with _ops.name_scope(name, 'Merge', inputs):
    val = _gen_logging_ops.merge_summary(inputs=inputs, name=name)
    _summary_op_util.collect(val, collections, [])
exit(val)
