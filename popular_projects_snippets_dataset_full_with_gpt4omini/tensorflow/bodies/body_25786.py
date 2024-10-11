# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
"""Reusable code for making a simple neural net layer."""
# Adding a name scope ensures logical grouping of the layers in the graph.
with tf.name_scope(layer_name):
    # This Variable will hold the state of the weights for the layer
    with tf.name_scope("weights"):
        weights = weight_variable([input_dim, output_dim])
    with tf.name_scope("biases"):
        biases = bias_variable([output_dim])
    with tf.name_scope("Wx_plus_b"):
        preactivate = tf.matmul(input_tensor, weights) + biases

    activations = act(preactivate)
    exit(activations)
