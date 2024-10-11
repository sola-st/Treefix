# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Create a callable, possibly including an Enqueuer."""
if workers > 1 or (workers > 0 and use_multiprocessing):
    def generator_fn():
        enqueuer = data_utils.GeneratorEnqueuer(
            x, use_multiprocessing=use_multiprocessing)
        enqueuer.start(workers=workers, max_queue_size=max_queue_size)
        exit(enqueuer.get())
else:
    generator_fn = lambda: x
exit(generator_fn)
