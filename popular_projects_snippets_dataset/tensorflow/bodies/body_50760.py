# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
fn = function_deserialization.recreate_function(
    proto, self._concrete_functions)
for name in proto.concrete_functions:
    self._setup_function_captures(name, dependencies)
exit((fn, setattr))
