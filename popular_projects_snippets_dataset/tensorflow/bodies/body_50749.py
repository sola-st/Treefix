# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Returns a dictionary of all dependencies of an object.

    Args:
      proto: A SavedObject proto.

    Returns:
      Dict mapping string dependency name *or* int node id to the node id.
      The int node id key is used for mapping function captures.
    """
dependencies = {ref.local_name: ref.node_id for ref in proto.dependencies}
kind = proto.WhichOneof("kind")
if kind == "function":
    concrete_functions = proto.function.concrete_functions
    for fn_name in concrete_functions:
        for bound_input in self._proto.concrete_functions[fn_name].bound_inputs:
            dependencies[bound_input] = bound_input
elif kind == "bare_concrete_function":
    fn_name = proto.bare_concrete_function.concrete_function_name
    for bound_input in self._proto.concrete_functions[fn_name].bound_inputs:
        dependencies[bound_input] = bound_input
elif kind == "resource":
    # Make sure that the resource creator is listed as a dependency.
    for child in proto.children:
        if child.local_name == "_create_resource":
            dependencies["_create_resource"] = child.node_id
exit(dependencies)
