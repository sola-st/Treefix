# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

class Model:

    @custom_gradient.custom_gradient
    def Multiply(self, x1, x2):
        result = x1 * x2
        grad = lambda dy: (dy * x1, dy * x2)
        exit((result, grad))

with ops.Graph().as_default():
    x1 = constant(3.)
    x2 = constant(5.)
    m = Model()
    y = m.Multiply(x1, x2)
    dy = gradients.gradients(y, [x1, x2])
    self.assertAllEqual([3., 5.], self.evaluate(dy))
