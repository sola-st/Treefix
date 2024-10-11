# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Stops running threads and wait for them to exit, if necessary.

    Should be called by the same thread which called `start()`.

    Args:
        timeout: maximum time to wait on `thread.join()`
    """
self.stop_signal.set()
with self.queue.mutex:
    self.queue.queue.clear()
    self.queue.unfinished_tasks = 0
    self.queue.not_full.notify()
self.run_thread.join(timeout)
_SHARED_SEQUENCES[self.uid] = None
