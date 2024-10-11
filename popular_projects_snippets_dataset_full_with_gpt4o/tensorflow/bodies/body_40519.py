# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = random_ops.random_uniform([2, 2])
with backprop.GradientTape() as g:
    y = random_ops.random_uniform([2])
with self.assertRaisesRegex(ValueError, 'must have rank at least 2'):
    g.batch_jacobian(y, x)
