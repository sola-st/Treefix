# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
if not test.is_gpu_available():
    with self.session(use_gpu=False):
        var = variables.Variable([True, False])
        update0 = state_ops.scatter_update(var, 1, True)
        update1 = state_ops.scatter_update(
            var, constant_op.constant(
                0, dtype=dtypes.int64), False)
        self.evaluate(var.initializer)

        self.evaluate([update0, update1])

        self.assertAllEqual([False, True], self.evaluate(var))
