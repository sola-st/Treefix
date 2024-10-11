# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
if context.executing_eagerly():
    # TODO(agarwal): b/128842926
    self.skipTest('Conversion of function calls not implemented yet.')
x = array_ops.ones((10, 2))
with backprop.GradientTape(persistent=False) as g:
    g.watch(x)
    with backprop.GradientTape(persistent=False) as gg:
        gg.watch(x)
        y = math_ops.reduce_sum(math_ops.square(x))
    dy_x = gg.jacobian(y, x)
dy_xx = g.batch_jacobian(dy_x, x)
dy_xx_answer = [[[2., 0], [0, 2.]]] * 10
self.assertAllClose(dy_xx_answer, self.evaluate(dy_xx))
