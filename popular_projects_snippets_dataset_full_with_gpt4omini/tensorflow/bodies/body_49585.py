# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
self.sequence = sequence
self.use_multiprocessing = use_multiprocessing

global _SEQUENCE_COUNTER
if _SEQUENCE_COUNTER is None:
    try:
        _SEQUENCE_COUNTER = multiprocessing.Value('i', 0)
    except OSError:
        # In this case the OS does not allow us to use
        # multiprocessing. We resort to an int
        # for enqueuer indexing.
        _SEQUENCE_COUNTER = 0

if isinstance(_SEQUENCE_COUNTER, int):
    self.uid = _SEQUENCE_COUNTER
    _SEQUENCE_COUNTER += 1
else:
    # Doing Multiprocessing.Value += x is not process-safe.
    with _SEQUENCE_COUNTER.get_lock():
        self.uid = _SEQUENCE_COUNTER.value
        _SEQUENCE_COUNTER.value += 1

self.workers = 0
self.executor_fn = None
self.queue = None
self.run_thread = None
self.stop_signal = None
