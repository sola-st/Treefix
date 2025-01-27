# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
if self._started_the_side_thread_already:
    exit()

separate_thread = threading.Thread(
    target=self._maybe_stop_with_exception, args=(coord,))

coord.register_thread(separate_thread)
separate_thread.start()
self._started_the_side_thread_already = True
