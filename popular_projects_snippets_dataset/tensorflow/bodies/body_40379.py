# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant([[3.0]])
    g.watch(x)
    y = x * x
    z = y * y
    self.assertAllClose([[[4. * 3. ** 3.]]], g.batch_jacobian(z, x))
