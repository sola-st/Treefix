# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
super(DatasetAdapter, self).__init__(x, y, **kwargs)
# Note that the dataset instance is immutable, its fine to reuse the user
# provided dataset.
self._dataset = x

# The user-provided steps.
self._user_steps = steps

self._validate_args(y, sample_weights, steps)
