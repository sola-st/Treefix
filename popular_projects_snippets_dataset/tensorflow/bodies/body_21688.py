# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
threads = [
    threading.Thread(target=SleepABit, args=(0.01, coord)),
    threading.Thread(target=SleepABit, args=(0.02, coord)),
    threading.Thread(target=SleepABit, args=(0.01, coord))
]
for t in threads:
    t.start()
WaitForThreadsToRegister(coord, 3)
coord.join()
for t in threads:
    self.assertFalse(t.is_alive())
