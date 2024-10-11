# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Reopens the EventFileWriter.

    Can be called after `close()` to add more events in the same directory.
    The events will go into a new events file.

    Does nothing if the EventFileWriter was not closed.
    """
self.event_writer.reopen()
self._closed = False
