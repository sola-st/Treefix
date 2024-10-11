# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
self.assertFalse(coord.should_stop())
self.assertFalse(coord.wait_for_stop(0.01))
coord.request_stop()
self.assertTrue(coord.should_stop())
self.assertTrue(coord.wait_for_stop(0.01))
