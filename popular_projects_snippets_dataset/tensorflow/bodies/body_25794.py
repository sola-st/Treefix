# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Runs the forward computation for a single dense layer."""
kernel, bias = weights
preactivate = tf.matmul(input_tensor, kernel) + bias

activations = act(preactivate)
exit(activations)
