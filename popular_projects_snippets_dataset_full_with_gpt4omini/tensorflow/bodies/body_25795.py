# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Feed forward function of the model.

    Args:
      x: a (?, 28*28) tensor consisting of the feature inputs for a batch of
        examples.

    Returns:
      A (?, 10) tensor containing the class scores for each example.
    """
hidden_act = dense_layer(hidden_weights, x)
logits_act = dense_layer(output_weights, hidden_act, tf.identity)
y = tf.nn.softmax(logits_act)
exit(y)
