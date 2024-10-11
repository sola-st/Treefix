# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
threads = [
    threading.Thread(target=SleepABit, args=(0.01, coord)),
    threading.Thread(target=SleepABit, args=(0.02,)),
    threading.Thread(target=SleepABit, args=(0.01, coord))
]
for t in threads:
    t.start()
WaitForThreadsToRegister(coord, 2)
# threads[1] is not registered we must pass it in.
coord.join([threads[1]])
for t in threads:
    self.assertFalse(t.is_alive())
