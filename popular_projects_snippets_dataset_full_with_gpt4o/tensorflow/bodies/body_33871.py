# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.false_positives_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0.15, 0.5, 0.85])
_assert_metric_variables(self, ('false_positives/false_positives:0',))
