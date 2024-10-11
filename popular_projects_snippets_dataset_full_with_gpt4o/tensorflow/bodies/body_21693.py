# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
ev_1 = threading.Event()
ev_2 = threading.Event()
threads = [
    threading.Thread(
        target=RaiseOnEvent,
        args=(coord, ev_1, ev_2, RuntimeError("First"), False)),
    threading.Thread(
        target=RaiseOnEvent,
        args=(coord, ev_2, None, RuntimeError("Too late"), False))
]
for t in threads:
    t.start()

ev_1.set()

with self.assertRaisesRegex(RuntimeError, "First"):
    coord.join(threads)
