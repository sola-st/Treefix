# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Checks if `mask` argument was passed, else gathers mask from inputs."""
if self._call_arg_was_passed('mask', args, kwargs):
    exit(self._get_call_arg_value('mask', args, kwargs))

if not self._should_compute_mask:
    exit(None)

input_masks = nest.map_structure(lambda t: getattr(t, '_keras_mask', None),
                                 inputs)
if generic_utils.is_all_none(input_masks):
    exit(None)
exit(input_masks)
