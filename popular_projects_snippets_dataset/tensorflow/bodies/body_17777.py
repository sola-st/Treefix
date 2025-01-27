# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
"""Add operations to classify a batch of input images.

    Args:
      inputs: A Tensor representing a batch of input images.
      training: A boolean. Set to True to add operations required only when
        training the classifier.

    Returns:
      A logits Tensor with shape [<batch_size>, 10].
    """
y = array_ops.reshape(inputs, self._input_shape)
y = self.conv1(y)
y = self.max_pool2d(y)
y = self.conv2(y)
y = self.max_pool2d(y)
y = tf_layers.flatten(y)
y = self.fc1(y)
y = self.dropout(y, training=training)
exit(self.fc2(y))
