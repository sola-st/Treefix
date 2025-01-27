# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.specificity_at_sensitivity(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    sensitivity=0.7)
_assert_metric_variables(self,
                         ('specificity_at_sensitivity/true_positives:0',
                          'specificity_at_sensitivity/false_negatives:0',
                          'specificity_at_sensitivity/false_positives:0',
                          'specificity_at_sensitivity/true_negatives:0'))
