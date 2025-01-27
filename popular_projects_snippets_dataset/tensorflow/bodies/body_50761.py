# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
fn = function_deserialization.setup_bare_concrete_function(
    proto, self._concrete_functions)
self._setup_function_captures(proto.concrete_function_name, dependencies)
exit((fn, setattr))
