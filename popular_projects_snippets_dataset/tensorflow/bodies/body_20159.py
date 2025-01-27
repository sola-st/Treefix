# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
blocking_end_time = time.time()
metrics.AddCheckpointWriteDuration(
    api_label=_ASYNC_CHECKPOINT_V1,
    microseconds=_get_duration_microseconds(blocking_start_time,
                                            blocking_end_time))
