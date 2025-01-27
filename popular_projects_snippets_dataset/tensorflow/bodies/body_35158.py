# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = [[1., 2, 3]]
b = [[2., 4, 3]]
dist = beta_lib.Beta(a, b, validate_args=True)
self.evaluate(dist.prob([.1, .3, .6]))
self.evaluate(dist.prob([.2, .3, .5]))
# Either condition can trigger.
with self.assertRaisesOpError("sample must be positive"):
    self.evaluate(dist.prob([-1., 0.1, 0.5]))
with self.assertRaisesOpError("sample must be positive"):
    self.evaluate(dist.prob([0., 0.1, 0.5]))
with self.assertRaisesOpError("sample must be less than `1`"):
    self.evaluate(dist.prob([.1, .2, 1.2]))
with self.assertRaisesOpError("sample must be less than `1`"):
    self.evaluate(dist.prob([.1, .2, 1.0]))
