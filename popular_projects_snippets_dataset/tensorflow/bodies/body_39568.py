# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Save the checkpointed variables.

    This method has exactly the same logic as save(), except it does not
    increment the underlying save_counter, which is done by the caller, e.g.,
    CheckpointManager.

    Args:
      save_path: The file prefix of the checkpoint file.
      options: Optional CheckpointOption instance.
      write_done_callback: Optional callback function executed after the async
        write is done.

    Returns:
      The full path of the checkpoint file.
    """
self._ensure_initialized()

write_start_time = time.time()

# Copy the variable values to the host CPU.
if self._writer_sem.acquire():
    self._copy_to_cpu()

# Trigger the async thread to checkpoint the cpu-copied variables.
# Need to wait until the weight copying finishes before checkpoint save.
context.async_wait()
self._save_file_prefix = save_path
self._use_checkpoint_save = False

# Ensure that we do not request async checkpointing to the underlying
# checkpointer as this could lead to an infinite loop.
self._checkpoint_options = copy.copy(options) if options else None
if self._checkpoint_options:
    self._checkpoint_options.experimental_enable_async_checkpoint = False

self._async_write_done_callback = write_done_callback
self._reader_sem.release()

write_end_time = time.time()
metrics.AddCheckpointWriteDuration(
    api_label=_ASYNC_CHECKPOINT,
    microseconds=_get_duration_microseconds(write_start_time,
                                            write_end_time))

exit(save_path)
