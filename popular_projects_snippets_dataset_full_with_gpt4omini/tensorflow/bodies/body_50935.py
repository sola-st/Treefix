# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(metrics.GetWrite(write_version="1"), 0)
metrics.IncrementWriteApi("foo")
self.assertEqual(metrics.GetWriteApi("foo"), 1)
metrics.IncrementWrite(write_version="1")
self.assertEqual(metrics.GetWrite(write_version="1"), 1)
