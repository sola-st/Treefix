# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.sensitivity_at_specificity(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    specificity=0.7)
_assert_metric_variables(self,
                         ('sensitivity_at_specificity/true_positives:0',
                          'sensitivity_at_specificity/false_negatives:0',
                          'sensitivity_at_specificity/false_positives:0',
                          'sensitivity_at_specificity/true_negatives:0'))
