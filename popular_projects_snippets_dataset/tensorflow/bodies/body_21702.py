# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
n = [3]
coord = coordinator.Coordinator()
thread = coordinator.LooperThread.loop(
    coord, 0, target=_StopAt0, args=(coord, n))
coord.join([thread])
self.assertEqual(0, n[0])
