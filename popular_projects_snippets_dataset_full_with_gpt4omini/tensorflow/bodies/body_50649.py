# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
self._warn_if_event_writer_is_closed()
super(FileWriter, self)._add_event(event, step)
