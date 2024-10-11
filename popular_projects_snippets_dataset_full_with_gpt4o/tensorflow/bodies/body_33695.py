# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    for label_dtype in (
        dtypes_lib.bool, dtypes_lib.int32, dtypes_lib.float32):
        predictions = constant_op.constant(
            [1, 0, 1, 0], shape=(1, 4), dtype=dtypes_lib.float32)
        labels = math_ops.cast(
            constant_op.constant([0, 1, 1, 0], shape=(1, 4)), dtype=label_dtype)
        auc, update_op = metrics.auc(labels, predictions)

        self.evaluate(variables.local_variables_initializer())
        self.assertAlmostEqual(0.5, self.evaluate(update_op))

        self.assertAlmostEqual(0.5, self.evaluate(auc))
