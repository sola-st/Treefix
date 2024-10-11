# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
super(ListsOfScalarsDataAdapter, self).__init__(x, y, **kwargs)
x = np.asarray(x)
if y is not None:
    y = np.asarray(y)
if sample_weights is not None:
    sample_weights = np.asarray(sample_weights)
sample_weight_modes = broadcast_sample_weight_modes(
    sample_weights, sample_weight_modes)

self._internal_adapter = TensorLikeDataAdapter(
    x,
    y=y,
    sample_weights=sample_weights,
    sample_weight_modes=sample_weight_modes,
    batch_size=batch_size,
    shuffle=shuffle,
    **kwargs)
