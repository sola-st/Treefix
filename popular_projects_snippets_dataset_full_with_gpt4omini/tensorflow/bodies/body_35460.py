# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
np.random.seed(1618)  # Make it reproducible.
num_samples = 21000

rand_probs = self._normalize(np.random.random_sample((10,)))
rand_probs2 = self._normalize(np.random.random_sample((3, 5)))  # batched
for probs in [[.5, .5], [.85, .05, .1], rand_probs, rand_probs2]:
    probs = np.asarray(probs)
    if len(probs.shape) == 1:
        probs = probs.reshape(1, probs.size)  # singleton batch

    logits = np.log(probs).astype(np.float32)
    composed_freqs = self._do_sampling(logits, num_samples, composed_sampler)
    native_freqs = self._do_sampling(logits, num_samples, native_sampler)

    # the test here is similar to core/lib/random/distribution_sampler_test.cc
    composed_chi2 = self._chi2(probs, composed_freqs)
    native_chi2 = self._chi2(probs, native_freqs)
    composed_native_chi2 = self._chi2(composed_freqs, native_freqs)

    def check(chi2s):
        for chi2 in chi2s:
            self.assertLess(chi2, 1e-3)

    check(composed_chi2)
    check(native_chi2)
    check(composed_native_chi2)
