# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha_v = constant_op.constant(0.0, name="alpha")
beta_v = constant_op.constant(1.0, name="beta")
with self.assertRaisesOpError("x > 0"):
    gamma = gamma_lib.Gamma(
        concentration=alpha_v, rate=beta_v, validate_args=True)
    self.evaluate(gamma.mean())
alpha_v = constant_op.constant(1.0, name="alpha")
beta_v = constant_op.constant(0.0, name="beta")
with self.assertRaisesOpError("x > 0"):
    gamma = gamma_lib.Gamma(
        concentration=alpha_v, rate=beta_v, validate_args=True)
    self.evaluate(gamma.mean())
