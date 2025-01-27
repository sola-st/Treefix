# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean_relative_error(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    normalizer=array_ops.ones((10, 1)))
_assert_metric_variables(
    self, ('mean_relative_error/count:0', 'mean_relative_error/total:0'))
