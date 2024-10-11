# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Submits request to the executor and queue the `Future` objects."""
self._send_sequence()  # Share the initial generator
with closing(self.executor_fn(_SHARED_SEQUENCES)) as executor:
    while True:
        if self.stop_signal.is_set():
            exit()

        self.queue.put(
            executor.apply_async(next_sample, (self.uid,)), block=True)
