# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.precision(
    predictions=array_ops.ones((10, 1)), labels=array_ops.ones((10, 1)))
_assert_metric_variables(self, ('precision/false_positives/count:0',
                                'precision/true_positives/count:0'))
