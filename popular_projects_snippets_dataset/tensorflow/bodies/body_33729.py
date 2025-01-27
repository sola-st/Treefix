# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for label_dtype in (dtypes_lib.bool, dtypes_lib.int32, dtypes_lib.float32):
    predictions_values = [
        0.0, 0.1, 0.2, 0.3, 0.4, 0.01, 0.02, 0.25, 0.26, 0.26]
    labels_values = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    weights_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    predictions = constant_op.constant(
        predictions_values, dtype=dtypes_lib.float32)
    labels = math_ops.cast(labels_values, dtype=label_dtype)
    weights = constant_op.constant(weights_values)
    specificity, update_op = metrics.sensitivity_at_specificity(
        labels, predictions, weights=weights, specificity=0.4)

    with self.cached_session():
        self.evaluate(variables.local_variables_initializer())
        self.assertAlmostEqual(0.675, self.evaluate(update_op))
        self.assertAlmostEqual(0.675, self.evaluate(specificity))
