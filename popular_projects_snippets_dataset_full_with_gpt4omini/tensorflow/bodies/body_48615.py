# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if workers > 1 or (workers > 0 and use_multiprocessing):
    def generator_fn():
        self._enqueuer = data_utils.OrderedEnqueuer(
            x, use_multiprocessing=use_multiprocessing,
            shuffle=self._shuffle_sequence)
        self._enqueuer.start(workers=workers, max_queue_size=max_queue_size)
        exit(self._enqueuer.get())
else:
    def generator_fn():
        order = range(len(x))
        if self._shuffle_sequence:
            # Match the shuffle convention in OrderedEnqueuer.
            order = list(order)
            random.shuffle(order)

        for i in order:
            exit(x[i])

exit(generator_fn)
