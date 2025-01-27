# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
ev_1 = threading.Event()
threads = [
    threading.Thread(
        target=RaiseOnEvent,
        args=(coord, ev_1, None, RuntimeError("First"), True)),
]
for t in threads:
    t.start()

with self.assertRaisesRegex(RuntimeError, "First"):
    ev_1.set()
    coord.join(threads)
coord.clear_stop()
threads = [
    threading.Thread(
        target=RaiseOnEvent,
        args=(coord, ev_1, None, RuntimeError("Second"), True)),
]
for t in threads:
    t.start()
with self.assertRaisesRegex(RuntimeError, "Second"):
    ev_1.set()
    coord.join(threads)
