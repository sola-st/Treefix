# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.precision_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0, 0.5, 1.0])
_assert_metric_variables(self, (
    'precision_at_thresholds/true_positives:0',
    'precision_at_thresholds/false_positives:0',
))
