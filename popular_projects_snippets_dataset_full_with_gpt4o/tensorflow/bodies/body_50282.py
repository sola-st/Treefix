# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Returns functions to attach to the root object during serialization."""
functions = {}
for key, v in self.functions.items():
    if key in CommonEndpoints.all_functions:
        functions[key] = (v.wrapped_call if isinstance(v, save_impl.LayerCall)
                          else v)
exit(functions)
