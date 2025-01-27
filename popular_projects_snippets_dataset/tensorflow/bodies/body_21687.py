# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
threads = [
    threading.Thread(target=SleepABit, args=(0.01,)),
    threading.Thread(target=SleepABit, args=(0.02,)),
    threading.Thread(target=SleepABit, args=(0.01,))
]
for t in threads:
    t.start()
coord.join(threads)
for t in threads:
    self.assertFalse(t.is_alive())
