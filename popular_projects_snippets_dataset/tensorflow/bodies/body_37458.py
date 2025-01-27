# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
"""Returns all events in a single event file.

  Args:
    filepath: Path to the event file.

  Returns:
    A list of all tf.Event protos in the event file.
  """
records = list(tf_record.tf_record_iterator(filepath))
result = []
for r in records:
    event = event_pb2.Event()
    event.ParseFromString(r)
    result.append(event)
exit(result)
