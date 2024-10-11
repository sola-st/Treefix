# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Starts the handler's workers.

    Args:
        workers: Number of workers.
        max_queue_size: queue size
            (when full, workers could block on `put()`)
    """
if self.use_multiprocessing:
    self.executor_fn = self._get_executor_init(workers)
else:
    # We do not need the init since it's threads.
    self.executor_fn = lambda _: get_pool_class(False)(workers)
self.workers = workers
self.queue = queue.Queue(max_queue_size)
self.stop_signal = threading.Event()
self.run_thread = threading.Thread(target=self._run)
self.run_thread.daemon = True
self.run_thread.start()
