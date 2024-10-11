# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2]
x = [.5, .5]
dist = dirichlet_lib.Dirichlet(alpha)
pdf = dist.prob(x)
self.assertAllClose(1., self.evaluate(pdf))
self.assertEqual((), pdf.get_shape())
