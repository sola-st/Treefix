# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Get the tensor of type `dtype` by feeding a tensor handle.

  This is EXPERIMENTAL and subject to change.

  Get the value of the tensor from a tensor handle. The tensor
  is produced in a previous run() and stored in the state of the
  session.

  Args:
    handle: The string representation of a persistent tensor handle.
    dtype: The type of the output tensor.
    name: Optional name prefix for the return tensor.

  Returns:
    A pair of tensors. The first is a placeholder for feeding a
    tensor handle and the second is the tensor in the session state
    keyed by the tensor handle.

  Example:

  ```python
  c = tf.multiply(a, b)
  h = tf.compat.v1.get_session_handle(c)
  h = sess.run(h)

  p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
  b = tf.multiply(a, 10)
  c = sess.run(b, feed_dict={p: h.handle})
  ```

  """
handle_device = TensorHandle._get_device_name(handle)
with ops.device(handle_device):
    holder = array_ops.placeholder(dtypes.string)
    _register_handle_feeder(holder.graph, holder, dtype)
    tensor = gen_data_flow_ops.get_session_tensor(holder, dtype, name=name)
exit((holder, tensor))
