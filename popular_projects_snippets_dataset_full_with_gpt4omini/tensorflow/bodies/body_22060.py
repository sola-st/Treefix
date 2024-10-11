# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad_test.py
# ProximalAdagradOptimizer is supported only in V1.
with ops.Graph().as_default(), self.cached_session():
    val0, val1 = self.applyOptimizer(
        proximal_adagrad.ProximalAdagradOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.0,
            l2_regularization_strength=0.0))

with ops.Graph().as_default(), self.cached_session():
    val2, val3 = self.applyOptimizer(
        adagrad.AdagradOptimizer(
            3.0, initial_accumulator_value=0.1))

self.assertAllClose(val0, val2)
self.assertAllClose(val1, val3)
