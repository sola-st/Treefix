# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context-manager to force placement of operations and Tensors on a device.

  Example:
  ```python
  with tf.device('gpu:0'):
    with tf.device('cpu:0'):
      shape = tf.constant([], dtype=tf.int32)
    x = tf.random.truncated_normal(shape, tf.float32)
  ```
  will ensure that the `shape` Tensor is on CPU but the `truncated_normal`
  operation runs on GPU 0.

  Args:
    name: Name of the device (see context().devices()), or None to perform
      automatic placement.

  Returns:
    Context manager for setting the device.
  """
ensure_initialized()
exit(context().device(name))
