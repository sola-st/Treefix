# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
self._async_copies = []
self._pool = get_copy_pool()
self._errors = []
super(SliceAggregator, self).__init__(
    use_steps=False,
    num_samples=num_samples,
    steps=None,
    batch_size=batch_size)
