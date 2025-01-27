# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Saves a training checkpoint and provides basic checkpoint management.

    The saved checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.save()` is
    called.

    `save` is a basic convenience wrapper around the `write` method,
    sequentially numbering checkpoints using `save_counter` and updating the
    metadata used by `tf.train.latest_checkpoint`. More advanced checkpoint
    management, for example garbage collection and custom numbering, may be
    provided by other utilities which also wrap `write`
    (`tf.train.CheckpointManager` for example).

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix). Names are generated based on this
        prefix and `Checkpoint.save_counter`.
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.

    Returns:
      The full path to the checkpoint.
    """
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
    if session is None:
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
file_path = self.write(
    "%s-%d" % (file_prefix, checkpoint_number), session=session)
checkpoint_management.update_checkpoint_state_internal(
    save_dir=os.path.dirname(file_prefix),
    model_checkpoint_path=file_path,
    all_model_checkpoint_paths=[file_path],
    save_relative_paths=True)
exit(file_path)
