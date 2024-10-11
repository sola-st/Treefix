# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for dtype in (dtypes_lib.bool, dtypes_lib.int32, dtypes_lib.float32):
    predictions = math_ops.cast(
        constant_op.constant([1, 0, 1, 0], shape=(1, 4)), dtype=dtype)
    labels = math_ops.cast(
        constant_op.constant([0, 1, 1, 0], shape=(1, 4)), dtype=dtype)
    recall, update_op = metrics.recall(labels, predictions)

    with self.cached_session():
        self.evaluate(variables.local_variables_initializer())
        self.assertAlmostEqual(0.5, self.evaluate(update_op))
        self.assertAlmostEqual(0.5, self.evaluate(recall))
