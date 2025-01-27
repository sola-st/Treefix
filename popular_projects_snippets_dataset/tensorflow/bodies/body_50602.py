# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_iterator.py
r = next(self._tf_record_iterator)
exit(event_pb2.Event.FromString(r))
