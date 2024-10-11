# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with self.session(use_gpu=use_gpu, graph=ops.Graph()) as sess:
    rng = random_ops.random_normal(
        [num], mean=mu, stddev=sigma, dtype=dtype, seed=seed)
    ret = np.empty([10, num])
    for i in range(10):
        ret[i, :] = self.evaluate(rng)
exit(ret)
