# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_adagrad_test.py
with self.session(), self.test_scope():
    val0, val1 = self.applyOptimizer(
        proximal_adagrad.ProximalAdagradOptimizer(
            3.0,
            initial_accumulator_value=0.1,
            l1_regularization_strength=0.0,
            l2_regularization_strength=0.0))

with self.session(), self.test_scope():
    val2, val3 = self.applyOptimizer(
        adagrad.AdagradOptimizer(
            3.0, initial_accumulator_value=0.1))

self.assertAllClose(val0, val2)
self.assertAllClose(val1, val3)
