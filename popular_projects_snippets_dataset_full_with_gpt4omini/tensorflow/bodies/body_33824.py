# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.percentage_below(values=array_ops.ones((10,)), threshold=2)
_assert_metric_variables(self, (
    'percentage_below_threshold/count:0',
    'percentage_below_threshold/total:0',
))
