# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
self.cls_ref = cls_ref
self.method_name = method_name
self.cls_symbol = (
    get_canonical_name_for_symbol(self.cls_ref,
                                  add_prefix_to_v1_names=True) or
    get_canonical_name_for_symbol(self.cls_ref,
                                  api_name='keras',
                                  add_prefix_to_v1_names=True))
if 'name' not in kwargs:
    kwargs['name'] = K.unique_object_name(
        'tf.' + self.cls_symbol + '.' + self.method_name, zero_based=True,
        avoid_observed_names=True)
kwargs['autocast'] = False

# Do not individually trace op layers in the SavedModel.
self._must_restore_from_config = True

super(ClassMethod, self).__init__(**kwargs)

# Preserve all argument data structures when saving/loading a config
# (e.g., don't unnest lists that contain one element)
self._preserve_input_structure_in_config = True

self._expects_training_arg = False
self._expects_mask_arg = False
