# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
grad = backprop.gradients_function(
    lambda x: array_ops.stop_gradient(math_ops.argmax(x)))
self.assertAllEqual(grad([0.0])[0], None)
