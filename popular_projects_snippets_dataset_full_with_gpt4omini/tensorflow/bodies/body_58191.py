# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
with self.assertRaises(ValueError):
    metrics.TFLiteMetrics(model_path='/path/to/model')
