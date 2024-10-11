# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
flat_outputs = nest.flatten(outputs)

mask_already_computed = (
    getattr(self, '_compute_output_and_mask_jointly', False) or
    all(getattr(x, '_keras_mask', None) is not None for x in flat_outputs))

# Only compute the mask if the Layer explicitly supports masking or has
# overridden `compute_mask`.
should_compute_mask = (
    hasattr(self, 'compute_mask') and
    (self.supports_masking or
     not getattr(self.compute_mask, '_is_default', False)))

if mask_already_computed:
    flat_masks = [getattr(x, '_keras_mask', None) for x in flat_outputs]
elif not should_compute_mask:
    flat_masks = [None for _ in flat_outputs]
else:
    output_masks = self.compute_mask(inputs, previous_mask)
    # `compute_mask` can return a single `None` even when a Layer
    # has multiple outputs.
    if output_masks is None:
        flat_masks = [None for _ in flat_outputs]
    else:
        flat_masks = nest.flatten(output_masks)

for output, mask in zip(flat_outputs, flat_masks):
    try:
        output._keras_mask = mask
    except AttributeError:
        # C Type such as np.ndarray.
        pass

if tf_utils.are_all_symbolic_tensors(flat_outputs):
    for output in flat_outputs:
        if getattr(output, '_keras_mask', None) is not None:
            # Do not track masks for `TensorFlowOpLayer` construction.
            output._keras_mask._keras_history_checked = True
