# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a_val = 1.
b_val = 2.
n_val = 100

random_seed.set_random_seed(654321)
beta1 = beta_lib.Beta(
    concentration1=a_val, concentration0=b_val, name="beta1")
samples1 = self.evaluate(beta1.sample(n_val, seed=123456))

random_seed.set_random_seed(654321)
beta2 = beta_lib.Beta(
    concentration1=a_val, concentration0=b_val, name="beta2")
samples2 = self.evaluate(beta2.sample(n_val, seed=123456))

self.assertAllClose(samples1, samples2)
