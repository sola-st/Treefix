# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Flushes the event file to disk and close the file.

    Call this method when you do not need the summary writer anymore.
    """
self.event_writer.close()
self._closed = True
