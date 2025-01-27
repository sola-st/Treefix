# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(metrics.GetReadFingerprint(), "")
metrics.SetReadFingerprint(saved_model_checksum="foo")
self.assertEqual(metrics.GetReadFingerprint(), "foo")

self.assertEqual(metrics.GetWriteFingerprint(), "")
metrics.SetWriteFingerprint(saved_model_checksum="foo")
self.assertEqual(metrics.GetWriteFingerprint(), "foo")
