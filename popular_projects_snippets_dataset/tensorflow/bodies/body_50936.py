# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(metrics.GetRead(write_version="2"), 0)
metrics.IncrementReadApi("bar")
self.assertEqual(metrics.GetReadApi("bar"), 1)
metrics.IncrementRead(write_version="2")
self.assertEqual(metrics.GetRead(write_version="2"), 1)
