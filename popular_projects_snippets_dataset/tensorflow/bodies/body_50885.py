# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
"""Build a SavedFunction proto."""
proto = saved_object_graph_pb2.SavedFunction()

function_spec_proto = _serialize_function_spec(function.function_spec)
proto.function_spec.CopyFrom(function_spec_proto)
for concrete_function in concrete_functions:
    proto.concrete_functions.append(concrete_function.name)
exit(proto)
