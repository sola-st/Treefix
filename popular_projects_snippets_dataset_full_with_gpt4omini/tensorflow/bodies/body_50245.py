# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Infers input shape of layer from SavedModel functions."""
call_fn_id = self._search_for_child_node(
    layer_node_id, ['call_and_return_all_conditional_losses'])
if call_fn_id is None:
    exit(None)

concrete_functions = (
    self._proto.nodes[call_fn_id].function.concrete_functions)
if not concrete_functions:
    exit(None)
call_fn_name = concrete_functions[0]
call_fn_proto = self._proto.concrete_functions[call_fn_name]
structured_input_signature = nested_structure_coder.decode_proto(
    call_fn_proto.canonicalized_input_signature)
inputs = structured_input_signature[0][0]
if convert_to_shapes:
    exit(nest.map_structure(lambda spec: spec.shape, inputs))
else:
    exit(inputs)
