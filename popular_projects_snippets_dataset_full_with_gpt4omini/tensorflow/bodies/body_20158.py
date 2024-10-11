# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
"""Run the saver process."""
logging.info("Saving checkpoints for %d into %s.", step, self._save_path)

start_time = time.time()
for l in self._listeners:
    l.before_save(session, step)

self._get_saver().save(session, self._save_path, global_step=step)
self._summary_writer.add_session_log(
    event_pb2.SessionLog(
        status=event_pb2.SessionLog.CHECKPOINT,
        checkpoint_path=self._save_path), step)

for l in self._listeners:
    l.after_save(session, step)

# Measure the async checkpoint write duration, i.e., non-blocking time.
end_time = time.time()
metrics.AddAsyncCheckpointWriteDuration(
    api_label=_ASYNC_CHECKPOINT_V1,
    microseconds=_get_duration_microseconds(start_time, end_time))

# Measure the elapsed time since the last checkpoint.
# Due to the nature of async checkpoint, here it actually captures the
# duration between the start_time of the previous checkpoint and the start
# time of this checkpoint. As a result, the duration of the final async
# checkpoint is excluded, which is fine since it does not take much time.
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    metrics.AddTrainingTimeSaved(
        api_label=_ASYNC_CHECKPOINT_V1,
        microseconds=_get_duration_microseconds(_END_TIME_OF_LAST_WRITE,
                                                start_time))
_END_TIME_OF_LAST_WRITE = start_time

logging.info("Checkpoint actual writing time: (%.3f sec)",
             end_time - start_time)
logging.info("Checkpoint finished for %d into %s.", step, self._save_path)
