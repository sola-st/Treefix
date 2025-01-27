# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if not is_none_or_empty(y):
    raise ValueError("`y` argument is not supported when using "
                     "`keras.utils.Sequence` as input.")
if not is_none_or_empty(sample_weights):
    raise ValueError("`sample_weight` argument is not supported when using "
                     "`keras.utils.Sequence` as input.")

self._size = len(x)
self._shuffle_sequence = shuffle
self._keras_sequence = x
self._enqueuer = None
super(KerasSequenceAdapter, self).__init__(
    x,
    shuffle=False,  # Shuffle is handed in the _make_callable override.
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    max_queue_size=max_queue_size,
    model=model,
    **kwargs)
