# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Stacks a list of rank `R` tensors into a rank `R+1` tensor.

  Args:
      x: List of tensors.
      axis: Axis along which to perform stacking.

  Returns:
      A tensor.

  Example:

      >>> a = tf.constant([[1, 2],[3, 4]])
      >>> b = tf.constant([[10, 20],[30, 40]])
      >>> tf.keras.backend.stack((a, b))
      <tf.Tensor: shape=(2, 2, 2), dtype=int32, numpy=
      array([[[ 1,  2],
              [ 3,  4]],
             [[10, 20],
              [30, 40]]], dtype=int32)>

  """
exit(array_ops.stack(x, axis=axis))
