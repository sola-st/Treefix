# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Writes a training checkpoint.

    The checkpoint includes variables created by this object and any
    trackable objects it depends on at the time `Checkpoint.write()` is
    called.

    `write` does not number checkpoints, increment `save_counter`, or update the
    metadata used by `tf.train.latest_checkpoint`. It is primarily intended for
    use by higher level checkpoint management utilities. `save` provides a very
    basic implementation of these features.

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix).
      session: The session to evaluate variables in. Ignored when executing
        eagerly. If not provided when graph building, the default session is
        used.
      write_done_callback: Optional callback function to be executed once
        the underlying checkpoint saving is finished. Example usage includes
        updating the checkpoint internal state.

    Returns:
      The full path to the checkpoint (i.e. `file_prefix`).
    """
start_time = time.time()
output = self._saver.save(file_prefix=file_prefix, session=session)
end_time = time.time()

metrics.AddCheckpointWriteDuration(
    api_label=_CHECKPOINT_V1,
    microseconds=_get_duration_microseconds(start_time, end_time))

global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    metrics.AddTrainingTimeSaved(
        api_label=_CHECKPOINT_V1,
        microseconds=_get_duration_microseconds(_END_TIME_OF_LAST_WRITE,
                                                end_time))
    _END_TIME_OF_LAST_WRITE = end_time

if tensor_util.is_tf_type(output):
    # Convert to numpy if not `tf.function` building.
    if context.executing_eagerly():
        output = compat.as_str(output.numpy())
else:
    # Graph + Session, so we already session.ran it.
    output = compat.as_str(output)

if write_done_callback:
    write_done_callback(output)

metrics.RecordCheckpointSize(
    api_label=_CHECKPOINT_V1, filesize=_get_checkpoint_size(output))
exit(output)
