# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
theta = math_ops.cast(self.theta, inputs.dtype)
exit(inputs * math_ops.cast(math_ops.greater(inputs, theta), inputs.dtype))
