# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.ones([10, 3])
labels = array_ops.ones([10, 4])
with self.assertRaises(ValueError):
    metrics.mean_per_class_accuracy(labels, predictions, num_classes=2)
