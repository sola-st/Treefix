# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = constant(1.0)
    y = x * 3.0
    grad = gradients.gradients(
        [y], [x], unconnected_gradients="zero")

    self.assertEqual(3.0, self.evaluate(grad)[0])
