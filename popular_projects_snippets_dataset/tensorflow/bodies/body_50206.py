# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/model_serialization.py
default_signature = None

# Create a default signature function if this is the only object in the
# cache (i.e. this is the root level object).
if len(serialization_cache[constants.KERAS_CACHE_KEY]) == 1:
    default_signature = save_impl.default_save_signature(self.obj)

# Other than the default signature function, all other attributes match with
# the ones serialized by Layer.
objects, functions = (
    super(ModelSavedModelSaver, self)._get_serialized_attributes_internal(
        serialization_cache))
functions['_default_save_signature'] = default_signature
exit((objects, functions))
