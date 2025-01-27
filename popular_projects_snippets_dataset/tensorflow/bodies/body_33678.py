# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.recall(
    predictions=array_ops.ones((10, 1)), labels=array_ops.ones((10, 1)))
_assert_metric_variables(
    self,
    ('recall/false_negatives/count:0', 'recall/true_positives/count:0'))
