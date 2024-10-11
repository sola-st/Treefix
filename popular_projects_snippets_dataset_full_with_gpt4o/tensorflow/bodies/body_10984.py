# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

@custom_gradient.custom_gradient
def MyIdentity(x):

    def Grad(dy):
        exit([3 * dy])

    exit((x, Grad))

with ops.Graph().as_default():
    x = constant(3.)
    y = MyIdentity(MyIdentity(x))
    dy = gradients.gradients(y, x)[0]
    with session.Session():
        self.assertEqual(9., self.evaluate(dy))
