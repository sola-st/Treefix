# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Flushes the event file to disk and close the file.

    Call this method when you do not need the summary writer anymore.
    """
if not self._closed:
    self.flush()
    self._try_put(self._close_sentinel)
    self._internal_close()
