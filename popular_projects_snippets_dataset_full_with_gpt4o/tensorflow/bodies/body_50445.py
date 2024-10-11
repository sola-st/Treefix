# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for `on_*_batch_end` methods."""
hook_name = 'on_{mode}_batch_end'.format(mode=mode)

if self._check_timing and batch >= 1:
    batch_time = time.time() - self._batch_start_time
    self._batch_times.append(batch_time)

self._call_batch_hook_helper(hook_name, batch, logs)

if len(self._batch_times) >= self._num_batches_for_timing_check:
    end_hook_name = hook_name
    begin_hook_name = 'on_{mode}_batch_begin'.format(mode=mode)
    avg_batch_time = sum(self._batch_times) / len(self._batch_times)
    avg_end_hook_time = sum(self._hook_times[end_hook_name]) / len(
        self._hook_times[end_hook_name])
    avg_begin_hook_time = sum(self._hook_times[begin_hook_name]) / len(
        self._hook_times[begin_hook_name])

    threshold_time = 1.0 * avg_batch_time
    warning_msg = ('Callback method `{hook}` is slow compared to '
                   'the batch time (batch time: {batch_time:.4f}s vs '
                   '`{hook}` time: {hook_time:.4f}s). Check your callbacks.')
    if avg_begin_hook_time > threshold_time:
        logging.warning(warning_msg.format(
            hook=begin_hook_name,
            batch_time=avg_batch_time,
            hook_time=avg_begin_hook_time))
    if avg_end_hook_time > threshold_time:
        logging.warning(warning_msg.format(
            hook=end_hook_name,
            batch_time=avg_batch_time,
            hook_time=avg_end_hook_time))
    self._check_timing = False
    self._batch_start_time = None
    self._batch_times = []
    self._hook_times = {}
