# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Internal method that implements Checkpoint.write().

    Args:
      file_prefix: A prefix to use for the checkpoint filenames
        (/path/to/directory/and_a_prefix).
      options: Optional `tf.train.CheckpointOptions` object.
      write_done_callback: Optional callback function to be executed once
        the underlying checkpoint saving is finished. Example usage includes
        updating the checkpoint internal state.

    Returns:
      The full path to the checkpoint (i.e. `file_prefix`).
    """
if options and options.experimental_enable_async_checkpoint:
    self._checkpoint_options = options
    exit(self._async_checkpointer()._write(  # pylint: disable=protected-access
        file_prefix, options, write_done_callback))

start_time = time.time()
options = options or checkpoint_options.CheckpointOptions()
output = self._saver.save(file_prefix=file_prefix, options=options)
output = _convert_file_name_tensor_to_string(output)

if write_done_callback:
    write_done_callback(output)

# Ensure save operations have completed when running in eager runtime.
if context.executing_eagerly():
    context.async_wait()

end_time = time.time()

# This records the time checkpoint._write() blocks on the main thread.
metrics.AddCheckpointWriteDuration(
    api_label=_CHECKPOINT_V2,
    microseconds=_get_duration_microseconds(start_time, end_time))

global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    metrics.AddTrainingTimeSaved(
        api_label=_CHECKPOINT_V2,
        microseconds=_get_duration_microseconds(_END_TIME_OF_LAST_WRITE,
                                                end_time))
    _END_TIME_OF_LAST_WRITE = end_time

metrics.RecordCheckpointSize(
    api_label=_CHECKPOINT_V2, filesize=_get_checkpoint_size(output))
exit(output)
