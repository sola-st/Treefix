# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Initializes the parameters for a single dense layer."""
initial_kernel = tf.keras.initializers.TruncatedNormal(
    mean=0.0, stddev=0.1, seed=RAND_SEED)
kernel = tf.Variable(initial_kernel([input_dim, output_dim]))
bias = tf.Variable(tf.constant(0.1, shape=[output_dim]))

exit((kernel, bias))
