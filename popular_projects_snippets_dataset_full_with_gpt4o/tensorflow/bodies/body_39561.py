# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""The thread function for the async checkpoint save."""
with context.executor_scope(
    executor.new_executor(
        enable_async=False, enable_streaming_enqueue=False)):
    while self._reader_sem.acquire() and not self._async_save_thread_shutdown:
        logging.info("Starting async checkpoint save on the device: %s",
                     self._default_device)

        async_save_start_time = time.time()

        # Specify the ops placement on the worker if running with
        # coordinator-worker mode. This is required as launching a new thread
        # would clear the placement policy and make localhost the default
        # placement, while the main thread's default placement would be the
        # master worker's CPU:0.
        with ops.device(self._default_device):
            if self._use_checkpoint_save:
                self._checkpoint.save(self._save_file_prefix,
                                      self._checkpoint_options)
            else:
                self._checkpoint._write(  # pylint: disable=protected-access
                    self._save_file_prefix,
                    options=self._checkpoint_options,
                    write_done_callback=self._async_write_done_callback)
        # Allow the next checkpoint event to overwrite the cpu-copied variables.
        self._writer_sem.release()

        async_save_end_time = time.time()
        metrics.AddAsyncCheckpointWriteDuration(
            api_label=_ASYNC_CHECKPOINT,
            microseconds=_get_duration_microseconds(async_save_start_time,
                                                    async_save_end_time))

        # Measure the elapsed time since the last checkpoint.
        # Due to the nature of async checkpoint, here it actually captures the
        # duration between the start_time of the previous checkpoint and the
        # start time of this checkpoint. As a result, the duration of the final
        # async checkpoint is excluded, which is fine since it does not take
        # much time.
        global _END_TIME_OF_LAST_ASYNC_WRITE
        with _END_TIME_OF_LAST_ASYNC_WRITE_LOCK:
            metrics.AddTrainingTimeSaved(
                api_label=_ASYNC_CHECKPOINT,
                microseconds=_get_duration_microseconds(
                    _END_TIME_OF_LAST_ASYNC_WRITE, async_save_start_time))
            _END_TIME_OF_LAST_ASYNC_WRITE = async_save_start_time
logging.info("Async save thread reached the end of the execution.")
