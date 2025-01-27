# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for label_dtype in (dtypes_lib.bool, dtypes_lib.int32, dtypes_lib.float32):
    predictions_values = [0.1, 0.2, 0.4, 0.3, 0.0, 0.1, 0.2, 0.2, 0.26, 0.26]
    labels_values = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    weights_values = [3]

    predictions = constant_op.constant(
        predictions_values, dtype=dtypes_lib.float32)
    labels = math_ops.cast(labels_values, dtype=label_dtype)
    weights = constant_op.constant(weights_values)
    specificity, update_op = metrics.specificity_at_sensitivity(
        labels, predictions, weights=weights, sensitivity=0.4)

    with self.cached_session():
        self.evaluate(variables.local_variables_initializer())

        self.assertAlmostEqual(0.6, self.evaluate(update_op))
        self.assertAlmostEqual(0.6, self.evaluate(specificity))
