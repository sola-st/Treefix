# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Registers `to_proto` and `from_proto` functions for collection_name.

  `to_proto` function converts a Python object to the corresponding protocol
  buffer, and returns the protocol buffer.

  `from_proto` function converts protocol buffer into a Python object, and
  returns the object..

  Args:
    collection_name: Name of the collection.
    proto_type: Protobuf type, such as `saver_pb2.SaverDef`,
      `variable_pb2.VariableDef`, `queue_runner_pb2.QueueRunnerDef`..
    to_proto: Function that implements Python object to protobuf conversion.
    from_proto: Function that implements protobuf to Python object conversion.
  """
if to_proto and not callable(to_proto):
    raise TypeError("to_proto must be callable.")
if from_proto and not callable(from_proto):
    raise TypeError("from_proto must be callable.")

_proto_function_registry.register((proto_type, to_proto, from_proto),
                                  collection_name)
