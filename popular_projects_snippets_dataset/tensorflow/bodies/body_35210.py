# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
# Corresponds to a uniform distribution
alpha = [1., 1, 1]
x = [[.2, .5, .3], [.3, .4, .3]]
dist = dirichlet_lib.Dirichlet(alpha)
pdf = dist.prob(x)
self.assertAllClose([2., 2.], self.evaluate(pdf))
self.assertEqual((2), pdf.get_shape())
