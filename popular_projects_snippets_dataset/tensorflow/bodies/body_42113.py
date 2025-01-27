# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
"""Returns all events in a single event file.

  Args:
    filepath: Path to the event file.

  Returns:
    A list of all tf.compat.v1.Event protos in the event file.
  """
records = list(tf.compat.v1.python_io.tf_record_iterator(filepath))
result = []
for r in records:
    event = tf.compat.v1.Event()
    event.ParseFromString(r)
    result.append(event)
exit(result)
