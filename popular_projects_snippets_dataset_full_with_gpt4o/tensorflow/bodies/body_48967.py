# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if not self._supports_masking and not self._expects_mask_arg:
    # Input masks only need to be retrieved if they are needed for `call`
    # or `compute_mask`.
    input_masks = None
    implicit_mask = False
elif self._call_arg_was_passed('mask', args, kwargs):
    input_masks = self._get_call_arg_value('mask', args, kwargs)
    implicit_mask = False
else:
    input_masks = [getattr(t, '_keras_mask', None) for t in input_list]
    if all(mask is None for mask in input_masks):
        input_masks = None
        implicit_mask = False
    else:
        # Only do expensive `nest` op when masking is actually being used.
        input_masks = nest.pack_sequence_as(inputs, input_masks)
        implicit_mask = True
exit((input_masks, implicit_mask))
