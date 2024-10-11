# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Setup captures and variables in a restored function."""
if concrete_function_name in self._restored_concrete_functions:
    exit()
self._restored_concrete_functions.add(concrete_function_name)
concrete_function = self._concrete_functions[concrete_function_name]
proto = self._proto.concrete_functions[concrete_function_name]
inputs = [nodes[node_id] for node_id in proto.bound_inputs]
function_saved_model_utils.restore_captures(concrete_function, inputs)
