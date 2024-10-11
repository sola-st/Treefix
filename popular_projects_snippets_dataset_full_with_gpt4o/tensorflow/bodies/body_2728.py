# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
self.assertIsInstance(tb, xla_client.Traceback)
self.assertIn(function, str(tb))
self.assertTrue(any(f.function_name == function for f in tb.frames))
