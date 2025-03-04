# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the cosine similarity between labels and predictions.

  Note that it is a number between -1 and 1. When it is a negative number
  between -1 and 0, 0 indicates orthogonality and values closer to -1
  indicate greater similarity. The values closer to 1 indicate greater
  dissimilarity. This makes it usable as a loss function in a setting
  where you try to maximize the proximity between predictions and
  targets. If either `y_true` or `y_pred` is a zero vector, cosine
  similarity will be 0 regardless of the proximity between predictions
  and targets.

  `loss = -sum(l2_norm(y_true) * l2_norm(y_pred))`

  Standalone usage:

  >>> y_true = [[0., 1.], [1., 1.], [1., 1.]]
  >>> y_pred = [[1., 0.], [1., 1.], [-1., -1.]]
  >>> loss = tf.keras.losses.cosine_similarity(y_true, y_pred, axis=1)
  >>> loss.numpy()
  array([-0., -0.999, 0.999], dtype=float32)

  Args:
    y_true: Tensor of true targets.
    y_pred: Tensor of predicted targets.
    axis: Axis along which to determine similarity.

  Returns:
    Cosine similarity tensor.
  """
y_true = nn.l2_normalize(y_true, axis=axis)
y_pred = nn.l2_normalize(y_pred, axis=axis)
exit(-math_ops.reduce_sum(y_true * y_pred, axis=axis))
