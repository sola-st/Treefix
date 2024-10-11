# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [[1., 2], [2., 3]]
x = [.5, .5]
pdf = dirichlet_lib.Dirichlet(alpha).prob(x)
self.assertAllClose([1., 3. / 2], self.evaluate(pdf))
self.assertEqual((2), pdf.get_shape())
