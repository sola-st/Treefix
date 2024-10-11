# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Save a training checkpoint.

    The saved checkpoint includes variables created by this object and any
    Trackable objects it depends on at the time `Saver.save()` is called.

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `checkpoint_number`, if provided.
      checkpoint_number: An integer variable or Tensor, used to number
        checkpoints. Typically this value is saved along with other variables in
        training checkpoints, which will happen automatically if it was created
        by `root_trackable` or one of its dependencies (via
        `Trackable._add_variable`).
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      The full path to the checkpoint.

    Raises:
      RuntimeError: if called in V1 Graph mode without a default session.
    """
options = options or checkpoint_options.CheckpointOptions()
feed_dict = {}
use_session = (not context.executing_eagerly() and
               not ops.inside_function())
if checkpoint_number:
    file_prefix = "%s-%d" % (file_prefix, checkpoint_number)
if use_session:
    if self._object_graph_feed_tensor is None:
        with ops.device("/cpu:0"):
            self._object_graph_feed_tensor = constant_op.constant(
                "", dtype=dtypes.string)
            self._file_prefix_feed_tensor = constant_op.constant(
                "", dtype=dtypes.string)
    object_graph_tensor = self._object_graph_feed_tensor
    file_prefix_tensor = self._file_prefix_feed_tensor
    feed_dict[file_prefix_tensor] = file_prefix
else:
    with ops.device("/cpu:0"):
        file_prefix_tensor = ops.convert_to_tensor(
            file_prefix, dtype=dtypes.string)
    object_graph_tensor = None

if not tensor_util.is_tensor(file_prefix):
    file_io.recursive_create_dir(os.path.dirname(file_prefix))

save_path, new_feed_additions = self._save_cached_when_graph_building(
    file_prefix_tensor, object_graph_tensor, options)

if new_feed_additions:
    feed_dict.update(new_feed_additions)
if not use_session:
    session = None
elif session is None:
    session = get_session()

if session:
    exit(session.run(save_path, feed_dict=feed_dict))
elif use_session:
    raise RuntimeError(f"Unable to save checkpoint to \"{file_prefix}\" "
                       "in graph mode without a default session. Please use "
                       "`with tf.Session():` to create a session.")
else:
    exit(save_path)
