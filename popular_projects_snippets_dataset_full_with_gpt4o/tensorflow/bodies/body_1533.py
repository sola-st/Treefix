# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/proximal_gradient_descent_test.py
with self.session(), self.test_scope():
    val0, val1 = self.applyOptimizer(
        proximal_gradient_descent.ProximalGradientDescentOptimizer(
            3.0,
            l1_regularization_strength=0.0,
            l2_regularization_strength=0.0))

with self.session(), self.test_scope():
    val2, val3 = self.applyOptimizer(
        gradient_descent.GradientDescentOptimizer(3.0))

self.assertAllClose(val0, val2)
self.assertAllClose(val1, val3)
