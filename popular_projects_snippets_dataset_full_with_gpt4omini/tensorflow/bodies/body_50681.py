# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
self._closed = True
self._worker.join()
self._ev_writer.Close()
