# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
"""Resets the MultiDeviceIterator in eager mode."""
if not ops.executing_eagerly_outside_functions():
    raise ValueError(
        "Resetting a multi-device iterator is only supported in the eager "
        "mode.")
# pylint: disable=protected-access
self._incarnation_id = gen_dataset_ops.multi_device_iterator_init(
    self._dataset._variant_tensor,
    self._multi_device_iterator_resource,
    max_buffer_size=self._max_buffer_size)
for i, device in enumerate(self._devices):
    with ops.device(device):
        ds = _create_device_dataset(self._prototype_device_datasets[i],
                                    self._incarnation_id,
                                    self._prefetch_buffer_size,
                                    self._experimental_slack)
        # Reset the device iterator resources with the new dataset.
        ds_variant = ds._variant_tensor
        gen_dataset_ops.make_iterator(
            ds_variant, self._device_iterators[i]._iterator_resource)
