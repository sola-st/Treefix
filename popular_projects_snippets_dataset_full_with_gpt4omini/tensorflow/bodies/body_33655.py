# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.ones((10, 3))
labels = array_ops.ones((10, 3))
weights = array_ops.ones((9, 3))
with self.assertRaises(ValueError):
    metrics.accuracy(labels, predictions, weights)
