# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
np.random.seed(1618)  # Make it reproducible.
num_samples = 40000

rand_probs = np.random.dirichlet([1., 1., 2., 3.])
rand_probs2 = np.random.dirichlet([1., 4., 5.], size=3)  # batched
for probs in [[.5, .5], [.85, .05, .1], rand_probs, rand_probs2]:
    probs = np.asarray(probs)
    if len(probs.shape) == 1:
        probs = probs.reshape(1, probs.size)  # singleton batch

    logits = np.log(probs).astype(np.float32)
    freqs = self._do_sampling(logits, num_samples)

    # the test here is similar to
    # python/kernel_tests/random/multinomial_op_test.py
    # Note that df >= 1 in all these cases. Choosing a cutoff of 1e-3
    # corresponds to an alpha value of 2.5% for df = 1, and smaller for larger
    # df.
    chi2 = self._chi2(probs, freqs)
    self.assertLess(chi2, 1e-3)
