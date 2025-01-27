# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of one vote falling into class k is the mean for class
# k.
alpha = [1., 2, 3]
with self.cached_session():
    for class_num in range(3):
        counts = np.zeros([3], dtype=np.float32)
        counts[class_num] = 1
        dist = ds.DirichletMultinomial(1., alpha)
        mean = dist.mean().eval()
        pmf = dist.prob(counts).eval()

        self.assertAllClose(mean[class_num], pmf)
        self.assertAllEqual([3], mean.shape)
        self.assertAllEqual([], pmf.shape)
