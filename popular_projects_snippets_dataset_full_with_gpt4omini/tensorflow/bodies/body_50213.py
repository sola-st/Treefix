# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py
"""Generates or retrieves serialized attributes from cache."""
keras_cache = serialization_cache.setdefault(constants.KERAS_CACHE_KEY, {})
if self.obj in keras_cache:
    exit(keras_cache[self.obj])

serialized_attr = keras_cache[self.obj] = (
    serialized_attributes.SerializedAttributes.new(self.obj))

if (save_impl.should_skip_serialization(self.obj) or
    self.obj._must_restore_from_config):  # pylint: disable=protected-access
    exit(serialized_attr)

object_dict, function_dict = self._get_serialized_attributes_internal(
    serialization_cache)

serialized_attr.set_and_validate_objects(object_dict)
serialized_attr.set_and_validate_functions(function_dict)
exit(serialized_attr)
