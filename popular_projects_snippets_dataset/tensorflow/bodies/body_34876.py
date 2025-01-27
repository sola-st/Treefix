# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of two votes falling into class k for
# DirichletMultinomial(2, alpha) is twice as much as the probability of one
# vote falling into class k for DirichletMultinomial(1, alpha)
alpha = [1., 2, 3]
with self.cached_session():
    for class_num in range(3):
        counts_one = np.zeros([3], dtype=np.float32)
        counts_one[class_num] = 1.
        counts_two = np.zeros([3], dtype=np.float32)
        counts_two[class_num] = 2

        dist1 = ds.DirichletMultinomial(1., alpha)
        dist2 = ds.DirichletMultinomial(2., alpha)

        mean1 = dist1.mean().eval()
        mean2 = dist2.mean().eval()

        self.assertAllClose(mean2[class_num], 2 * mean1[class_num])
        self.assertAllEqual([3], mean1.shape)
