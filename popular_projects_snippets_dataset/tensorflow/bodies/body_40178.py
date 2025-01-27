# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/cancellation_test.py
manager = cancellation.CancellationManager()
self.assertFalse(manager.is_cancelled)
manager.start_cancel()
self.assertTrue(manager.is_cancelled)
