# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self._pop_writer()

if self._is_tracing:
    self._stop_trace()

self._close_writers()
self._delete_tmp_write_dir()
