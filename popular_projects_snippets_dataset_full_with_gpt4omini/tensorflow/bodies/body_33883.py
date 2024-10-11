# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.true_positives(
    labels=(0, 1, 0, 1),
    predictions=(0, 0, 1, 1))
_assert_metric_variables(self, ('true_positives/count:0',))
