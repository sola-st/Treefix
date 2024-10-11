# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
"""Build a SavedConcreteFunction."""
bound_inputs = []
try:
    for capture in concrete_function.captured_inputs:
        bound_inputs.append(node_ids[capture])
except KeyError:
    raise KeyError(
        f"Failed to add concrete function '{concrete_function.name}' to object-"
        f"based SavedModel as it captures tensor {capture!r} which is unsupported"
        " or not reachable from root. "
        "One reason could be that a stateful object or a variable that the "
        "function depends on is not assigned to an attribute of the serialized "
        "trackable object (see SaveTest.test_captures_unreachable_variable).")
concrete_function_proto = saved_object_graph_pb2.SavedConcreteFunction()
structured_outputs = func_graph_module.convert_structure_to_signature(
    concrete_function.structured_outputs)
concrete_function_proto.canonicalized_input_signature.CopyFrom(
    nested_structure_coder.encode_structure(
        concrete_function.structured_input_signature))
concrete_function_proto.output_signature.CopyFrom(
    nested_structure_coder.encode_structure(structured_outputs))
concrete_function_proto.bound_inputs.extend(bound_inputs)
exit(concrete_function_proto)
