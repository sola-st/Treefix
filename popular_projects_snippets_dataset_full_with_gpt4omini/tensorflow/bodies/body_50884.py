# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
"""Build a SavedBareConcreteFunction."""
# pylint: disable=protected-access
proto = saved_object_graph_pb2.SavedBareConcreteFunction(
    concrete_function_name=concrete_function.name,
    allowed_positional_arguments=concrete_function._num_positional_args,
    argument_keywords=concrete_function._arg_keywords)
if concrete_function._pre_initialized_function_spec is not None:
    proto.function_spec.CopyFrom(
        _serialize_function_spec(
            concrete_function._pre_initialized_function_spec))
exit(proto)
