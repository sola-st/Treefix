# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
self._enqueuer = data_utils.OrderedEnqueuer(
    x, use_multiprocessing=use_multiprocessing,
    shuffle=self._shuffle_sequence)
self._enqueuer.start(workers=workers, max_queue_size=max_queue_size)
exit(self._enqueuer.get())
