# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [[1., 2, 3]]
dist = dirichlet_lib.Dirichlet(alpha, validate_args=True)
self.evaluate(dist.prob([.1, .3, .6]))
self.evaluate(dist.prob([.2, .3, .5]))
# Either condition can trigger.
with self.assertRaisesOpError("samples must be positive"):
    self.evaluate(dist.prob([-1., 1.5, 0.5]))
with self.assertRaisesOpError("samples must be positive"):
    self.evaluate(dist.prob([0., .1, .9]))
with self.assertRaisesOpError("sample last-dimension must sum to `1`"):
    self.evaluate(dist.prob([.1, .2, .8]))
