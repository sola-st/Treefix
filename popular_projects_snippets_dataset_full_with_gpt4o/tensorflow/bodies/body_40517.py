# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = random_ops.random_uniform([2, 3])
with backprop.GradientTape() as g:
    y = array_ops.concat([x, x], axis=0)
with self.assertRaisesRegex(ValueError, 'Need first dimension'):
    g.batch_jacobian(y, x)
