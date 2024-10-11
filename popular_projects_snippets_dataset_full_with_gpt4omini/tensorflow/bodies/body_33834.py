# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.ones([10])
labels = array_ops.ones([10])
weights = array_ops.zeros([9])
with self.assertRaises(ValueError):
    metrics.mean_iou(labels, predictions, num_classes=2, weights=weights)
