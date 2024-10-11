# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
ev_1 = threading.Event()
threads = [
    threading.Thread(
        target=RaiseOnEvent,
        args=(coord, ev_1, None,
              errors_impl.OutOfRangeError(None, None, "First"), True))
]
for t in threads:
    t.start()

ev_1.set()
coord.join(threads)
