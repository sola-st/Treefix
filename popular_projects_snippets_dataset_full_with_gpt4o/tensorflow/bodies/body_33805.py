# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.root_mean_squared_error(
    predictions=array_ops.ones((10, 1)), labels=array_ops.ones((10, 1)))
_assert_metric_variables(
    self,
    ('root_mean_squared_error/count:0', 'root_mean_squared_error/total:0'))
