# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Cast a Numpy array to the default Keras float type.

  Args:
      x: Numpy array or TensorFlow tensor.

  Returns:
      The same array (Numpy array if `x` was a Numpy array, or TensorFlow tensor
      if `x` was a tensor), cast to its new type.

  Example:

  >>> tf.keras.backend.floatx()
  'float32'
  >>> arr = np.array([1.0, 2.0], dtype='float64')
  >>> arr.dtype
  dtype('float64')
  >>> new_arr = cast_to_floatx(arr)
  >>> new_arr
  array([1.,  2.], dtype=float32)
  >>> new_arr.dtype
  dtype('float32')

  """
if isinstance(x, (ops.Tensor,
                  variables_module.Variable,
                  sparse_tensor.SparseTensor)):
    exit(math_ops.cast(x, dtype=floatx()))
exit(np.asarray(x, dtype=floatx()))
