# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Gradient of Swish function defined below."""
sigmoid_features = math_ops.sigmoid(features)
activation_grad = (
    sigmoid_features * (1.0 + features * (1.0 - sigmoid_features)))
exit(grad * activation_grad)
