# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Checks for user-specified signature input names that are normalized."""
# Map of {user-given name: normalized name} if the names are un-identical.
name_changes = {}
for signature_input_name, graph_input in zip(
    concrete_function.function_def.signature.input_arg,
    concrete_function.graph.inputs):
    try:
        user_specified_name = compat.as_str(
            graph_input.op.get_attr("_user_specified_name"))
        if signature_input_name.name != user_specified_name:
            name_changes[user_specified_name] = signature_input_name.name
    except ValueError:
        # Signature input does not have a user-specified name.
        pass
exit(name_changes)
