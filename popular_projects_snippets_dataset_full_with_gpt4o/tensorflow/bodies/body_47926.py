# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
self.attr_name = attr_name

if 'name' not in kwargs:
    kwargs['name'] = K.unique_object_name(
        'input.' + self.attr_name, zero_based=True, avoid_observed_names=True)
kwargs['autocast'] = False

# Do not individually trace op layers in the SavedModel.
self._must_restore_from_config = True

super(InstanceProperty, self).__init__(**kwargs)

# Preserve all argument data structures when saving/loading a config
# (e.g., don't unnest lists that contain one element)
self._preserve_input_structure_in_config = True
