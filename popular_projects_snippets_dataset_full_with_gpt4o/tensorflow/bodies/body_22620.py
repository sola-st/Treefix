# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
"""Tests the new FTRL op with support for l2 shrinkage on sparse grads."""
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32]:
        with self.cached_session():
            var0 = variables.Variable([[1.0], [2.0]], dtype=dtype)
            var1 = variables.Variable([[4.0], [3.0]], dtype=dtype)
            grads0 = indexed_slices.IndexedSlices(
                constant_op.constant([0.1], shape=[1, 1], dtype=dtype),
                constant_op.constant([0]), constant_op.constant([2, 1]))
            grads1 = indexed_slices.IndexedSlices(
                constant_op.constant([0.02], shape=[1, 1], dtype=dtype),
                constant_op.constant([1]), constant_op.constant([2, 1]))

            opt = ftrl.FtrlOptimizer(
                3.0,
                initial_accumulator_value=0.1,
                l1_regularization_strength=0.001,
                l2_regularization_strength=2.0,
                l2_shrinkage_regularization_strength=0.1)
            update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType([[1.0], [2.0]], v0_val)
            self.assertAllCloseAccordingToType([[4.0], [3.0]], v1_val)

            # Run 10 steps FTRL
            for _ in range(10):
                update.run()

            v0_val, v1_val = self.evaluate([var0, var1])
            self.assertAllCloseAccordingToType([[-0.22578995], [2.]], v0_val)
            self.assertAllCloseAccordingToType([[4.], [-0.13229476]], v1_val)
