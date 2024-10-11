# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Get id of current thread, suitable for logging as an unsigned quantity."""
thread_id = _thread.get_ident()
exit(thread_id & _THREAD_ID_MASK)
