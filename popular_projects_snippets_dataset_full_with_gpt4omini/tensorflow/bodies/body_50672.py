# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer_v2.py
"""Flushes the event file to disk and close the file.

    Call this method when you do not need the summary writer anymore.
    """
if not self._closed:
    self.flush()
    self._session.run(self._close_op)
    self._closed = True
