# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean_cosine_distance(
    predictions=array_ops.ones((10, 3)),
    labels=array_ops.ones((10, 3)),
    dim=1)
_assert_metric_variables(self, (
    'mean_cosine_distance/count:0',
    'mean_cosine_distance/total:0',
))
