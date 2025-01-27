# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.false_negatives(
    labels=(0, 1, 0, 1),
    predictions=(0, 0, 1, 1))
_assert_metric_variables(self, ('false_negatives/count:0',))
