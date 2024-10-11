# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
wait_for_stop_ev = threading.Event()
has_stopped_ev = threading.Event()
threads = [
    threading.Thread(
        target=StopOnEvent,
        args=(coord, wait_for_stop_ev, has_stopped_ev)),
    threading.Thread(target=SleepABit, args=(10.0,))
]
for t in threads:
    t.daemon = True
    t.start()
wait_for_stop_ev.set()
has_stopped_ev.wait()
with self.assertRaisesRegex(RuntimeError, "threads still running"):
    coord.join(threads, stop_grace_period_secs=stop_grace_period)
