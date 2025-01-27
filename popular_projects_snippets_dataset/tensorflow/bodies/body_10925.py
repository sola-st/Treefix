# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = constant(1.0, shape=[2, 2])
    y = constant(3.0, shape=[3, 1])
    grads = gradients.gradients(
        [y], [x], unconnected_gradients="zero")

    self.assertAllEqual([[0.0, 0.0], [0.0, 0.0]], self.evaluate(grads)[0])
