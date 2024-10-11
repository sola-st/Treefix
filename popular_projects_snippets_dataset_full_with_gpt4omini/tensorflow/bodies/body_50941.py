# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
self.assertEqual(
    metrics.GetCheckpointSize(api_label="baz", filesize=100), 0)
metrics.RecordCheckpointSize(api_label="baz", filesize=100)
metrics.RecordCheckpointSize(api_label="baz", filesize=100)
self.assertEqual(
    metrics.GetCheckpointSize(api_label="baz", filesize=100), 2)
