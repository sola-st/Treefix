# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
super(CompositeTensorDataAdapter, self).__init__(x, y, **kwargs)
x, y, sample_weights = _process_tensorlike((x, y, sample_weights))
sample_weight_modes = broadcast_sample_weight_modes(
    sample_weights, sample_weight_modes)

# If sample_weights are not specified for an output use 1.0 as weights.
(sample_weights, _, _) = training_utils.handle_partial_sample_weights(
    y, sample_weights, sample_weight_modes, check_all_flat=True)

inputs = pack_x_y_sample_weight(x, y, sample_weights)

dataset = dataset_ops.DatasetV2.from_tensor_slices(inputs)
num_samples = int(nest.flatten(x)[0].shape[0])
if shuffle:
    dataset = dataset.shuffle(num_samples)

# If batch_size is not passed but steps is, calculate from the input data.
# Default to 32 for backwards compat.
if not batch_size:
    batch_size = int(math.ceil(num_samples / steps)) if steps else 32

dataset = dataset.batch(batch_size)
self._size = int(math.ceil(num_samples / batch_size))
self._batch_size = batch_size
self._has_partial_batch = (self._size != (num_samples // batch_size))

self._partial_batch_size = None
if self._has_partial_batch:
    self._partial_batch_size = (
        num_samples - (self._size - 1) * self._batch_size)

self._dataset = dataset
