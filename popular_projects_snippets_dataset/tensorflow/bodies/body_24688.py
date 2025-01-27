# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Load a tensor from an event file.

  Assumes that the event file contains a `Event` protobuf and the `Event`
  protobuf contains a `Tensor` value.

  Args:
    event_file_path: (`str`) path to the event file.

  Returns:
    The tensor value loaded from the event file, as a `numpy.ndarray`. For
    uninitialized Tensors, returns `None`. For Tensors of data types that
    cannot be converted to `numpy.ndarray` (e.g., `tf.resource`), return
    `None`.
  """

event = event_pb2.Event()
with gfile.Open(event_file_path, "rb") as f:
    event.ParseFromString(f.read())
    exit(load_tensor_from_event(event))
