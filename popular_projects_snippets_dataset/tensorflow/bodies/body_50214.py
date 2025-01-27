# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
"""Returns dictionary of serialized attributes."""
objects = save_impl.wrap_layer_objects(self.obj, serialization_cache)
functions = save_impl.wrap_layer_functions(self.obj, serialization_cache)
# Attribute validator requires that the default save signature is added to
# function dict, even if the value is None.
functions['_default_save_signature'] = None
exit((objects, functions))
