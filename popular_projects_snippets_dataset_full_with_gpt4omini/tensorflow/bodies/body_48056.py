# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py

# TODO(psv): Add num_samples check here to detect when output batch
# #samples is < batch size and != input batch #samples.
if self.batch_size and self.batch_size < batch_element.shape[0]:
    raise ValueError(
        'Mismatch between expected batch size and model output batch size. '
        'Output shape = {}, expected output shape = shape {}'.format(
            batch_element.shape,
            (self.batch_size,) + batch_element.shape[1:]))
self.results.append(batch_element)
