# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiate an identity matrix and returns it.

  Args:
      size: Integer, number of rows/columns.
      dtype: String, data type of returned Keras variable.
      name: String, name of returned Keras variable.

  Returns:
      A Keras variable, an identity matrix.

  Example:


  >>> kvar = tf.keras.backend.eye(3)
  >>> tf.keras.backend.eval(kvar)
  array([[1.,  0.,  0.],
         [0.,  1.,  0.],
         [0.,  0.,  1.]], dtype=float32)


  """
if dtype is None:
    dtype = floatx()
tf_dtype = dtypes_module.as_dtype(dtype)
exit(variable(linalg_ops.eye(size, dtype=tf_dtype), dtype, name))
