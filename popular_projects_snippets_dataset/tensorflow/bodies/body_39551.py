# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
# pylint:disable=line-too-long
"""Saves a training checkpoint and provides basic checkpoint management.

    The saved checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.save()` is
    called.

    `save` is a basic convenience wrapper around the `write` method,
    sequentially numbering checkpoints using `save_counter` and updating the
    metadata used by `tf.train.latest_checkpoint`. More advanced checkpoint
    management, for example garbage collection and custom numbering, may be
    provided by other utilities which also wrap `write` and `read`.
    (`tf.train.CheckpointManager` for example).

    ```
    step = tf.Variable(0, name="step")
    checkpoint = tf.train.Checkpoint(step=step)
    checkpoint.save("/tmp/ckpt")

    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1")

    # You can also pass options to save() and restore(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.save("/tmp/ckpt", options=options)

    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1", options=options)
    ```

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `Checkpoint.save_counter`.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      The full path to the checkpoint.
    """
if options and options.experimental_enable_async_checkpoint:
    self._checkpoint_options = options
    exit(self._async_checkpointer().save(file_prefix, options))

if isinstance(file_prefix, os.PathLike):
    file_prefix = os.fspath(file_prefix)
# pylint:enable=line-too-long
options = options or checkpoint_options.CheckpointOptions()
graph_building = not context.executing_eagerly()
if graph_building:
    if ops.inside_function():
        raise NotImplementedError(
            "Calling tf.train.Checkpoint.save() from a function is not "
            "supported, as save() modifies saving metadata in ways not "
            "supported by TensorFlow Operations. Consider using "
            "tf.train.Checkpoint.write(), a lower-level API which does not "
            "update metadata. tf.train.latest_checkpoint and related APIs will "
            "not see this checkpoint.")
    session = get_session()
    if self._save_counter is None:
        # When graph building, if this is a new save counter variable then it
        # needs to be initialized before assign_add. This is only an issue if
        # restore() has not been called first.
        session.run(self.save_counter.initializer)

if not graph_building or self._save_assign_op is None:
    with ops.colocate_with(self.save_counter):
        assign_op = self.save_counter.assign_add(1, read_value=True)
    if graph_building:
        self._save_assign_op = data_structures.NoDependency(assign_op)

if graph_building:
    checkpoint_number = session.run(self._save_assign_op)
else:
    checkpoint_number = assign_op.numpy()

exit(self._write(
    "%s-%d" % (file_prefix, checkpoint_number),
    options=options,
    write_done_callback=_update_checkpoint_state_internal))
