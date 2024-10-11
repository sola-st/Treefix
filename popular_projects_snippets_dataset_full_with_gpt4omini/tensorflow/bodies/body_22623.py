# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
# The v1 optimizers do not support eager execution
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32]:
        with self.cached_session():
            val0, val1 = self.applyOptimizer(
                ftrl.FtrlOptimizer(
                    3.0,
                    # Adagrad learning rate
                    learning_rate_power=-0.5,
                    initial_accumulator_value=0.1,
                    l1_regularization_strength=0.0,
                    l2_regularization_strength=0.0),
                dtype)

        with self.cached_session():
            val2, val3 = self.applyOptimizer(
                adagrad.AdagradOptimizer(3.0, initial_accumulator_value=0.1),
                dtype)

        self.assertAllCloseAccordingToType(val0, val2, half_rtol=2e-3)
        self.assertAllCloseAccordingToType(val1, val3, half_rtol=2e-3)
