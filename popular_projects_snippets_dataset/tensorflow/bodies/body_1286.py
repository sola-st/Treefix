# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
def f(x):
    exit(x)

with self.test_scope():
    grad_fn = backprop.gradients_function(f)
    self.assertAllEqual(2., grad_fn(1., dy=2.)[0])
