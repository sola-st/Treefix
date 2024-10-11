# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Many `Layer`s don't need to call `compute_mask`.
# This method is optimized to do as little work as needed for the common
# case.
if not self._supports_masking:
    exit()

flat_outputs = nest.flatten(outputs)

mask_already_computed = (
    getattr(self, '_compute_output_and_mask_jointly', False) or
    all(getattr(x, '_keras_mask', None) is not None for x in flat_outputs))
if mask_already_computed:
    if build_graph:
        self._set_mask_keras_history_checked(flat_outputs)
    exit()

output_masks = self.compute_mask(inputs, previous_mask)
if output_masks is None:
    exit()

flat_masks = nest.flatten(output_masks)
for tensor, mask in zip(flat_outputs, flat_masks):
    try:
        tensor._keras_mask = mask
    except AttributeError:
        # C Type such as np.ndarray.
        pass

if build_graph:
    self._set_mask_keras_history_checked(flat_outputs)
