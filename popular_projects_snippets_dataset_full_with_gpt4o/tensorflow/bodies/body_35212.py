# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2]
x = [[.5, .5], [.2, .8]]
pdf = dirichlet_lib.Dirichlet(alpha).prob(x)
self.assertAllClose([1., 8. / 5], self.evaluate(pdf))
self.assertEqual((2), pdf.get_shape())
