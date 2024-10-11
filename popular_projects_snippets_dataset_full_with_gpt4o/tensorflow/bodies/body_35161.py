# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
# This is equivalent to a uniform distribution
a = 1.
b = 1.
x = np.array([.1, .2, .3, .5, .8], dtype=np.float32)
dist = beta_lib.Beta(a, b)
pdf = dist.prob(x)
self.assertAllClose([1.] * 5, self.evaluate(pdf))
self.assertEqual((5,), pdf.get_shape())
