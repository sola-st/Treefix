# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Join the async save thread.

    The steps for terminating the async save thread:
    1). Wait until the last async save event is done.
    2). Set _async_save_thread_shutdown flag to false to indicate termination.
    3). Trigger the async save thread to check and fail the while-predicate.
    4). Join the async save thread. (The thread may finish before joining.)
    """
if self._writer_sem.acquire(timeout=3600):  # Step-1.
    self._async_save_thread_shutdown = True  # Step-2.
    self._reader_sem.release()  # Step-3.
    logging.info("Joining the async save thread.")
    if self._async_save_thread is not None:
        self._async_save_thread.join()  # Step-4.
else:
    logging.error("Timeout waiting for the async save thread; terminating the"
                  " thread instead. The last checkpoint may be incomeplete.")
