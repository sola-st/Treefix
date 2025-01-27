# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Calculates cross entropy loss.

    Args:
      probs: Class probabilities predicted by the model. The shape is expected
        to be (?, 10).
      labels: Truth labels for the classes, as one-hot encoded vectors. The
        shape is expected to be the same as `probs`.

    Returns:
      A scalar loss tensor.
    """
diff = -labels * tf.math.log(probs)
loss = tf.reduce_mean(diff)
exit(loss)
