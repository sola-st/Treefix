# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/identity_bijector_test.py
with self.cached_session():
    bijector = identity_bijector.Identity()
    bijector_test_util.assert_scalar_congruency(
        bijector, lower_x=-2., upper_x=2.)
