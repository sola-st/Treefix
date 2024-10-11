# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Save the checkpointed variables.

    Args:
      save_path: The file prefix of the checkpoint file.
      options: Optional CheckpointOption instance.

    Returns:
      The full path of the checkpoint file.
    """
# If this is the first time that AsyncCheckpoint.save() is called,
# initialize the cpu-copied variables and create the pair-wise mapping
# between the original model variables and the cpu-copied variables.
#
# This is not performed in the initializer because some variables, e.g.,
# slot variables of the optimizer, were not created until actually running
# the train function, so we could only get the complete list of the
# variables after some train steps were run.
self._ensure_initialized()

save_start_time = time.time()

# Copy the variable values to the host CPU.
if self._writer_sem.acquire():
    self._copy_to_cpu()

# Retrieve the save counter from the underlying checkpoint object to
# re-construct the full path of the checkpoint file.
# This step has to happen before triggerting the underlying checkpoint;
# otherwise, the save_counter value may or may not have been updated.
save_counter = self._checkpoint.save_counter.numpy() + 1
full_path = "{}-{}".format(save_path, save_counter)

# Trigger the async thread to checkpoint the cpu-copied variables.
# Need to wait until the weight copying finishes before checkpoint save.
context.async_wait()
self._save_file_prefix = save_path
self._use_checkpoint_save = True

# Ensure that we do not request async checkpointing to the underlying
# checkpointer as this could lead to an infinite loop.
self._checkpoint_options = copy.copy(options) if options else None
if self._checkpoint_options:
    self._checkpoint_options.experimental_enable_async_checkpoint = False

self._reader_sem.release()

save_end_time = time.time()
metrics.AddCheckpointWriteDuration(
    api_label=_ASYNC_CHECKPOINT,
    microseconds=_get_duration_microseconds(save_start_time, save_end_time))

exit(full_path)
