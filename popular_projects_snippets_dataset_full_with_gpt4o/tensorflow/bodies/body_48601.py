# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
enqueuer = data_utils.GeneratorEnqueuer(
    x, use_multiprocessing=use_multiprocessing)
enqueuer.start(workers=workers, max_queue_size=max_queue_size)
exit(enqueuer.get())
