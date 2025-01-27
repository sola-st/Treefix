# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates an all-ones variable and returns it.

  Args:
      shape: Tuple of integers, shape of returned Keras variable.
      dtype: String, data type of returned Keras variable.
      name: String, name of returned Keras variable.

  Returns:
      A Keras variable, filled with `1.0`.
      Note that if `shape` was symbolic, we cannot return a variable,
      and will return a dynamically-shaped tensor instead.

  Example:


  >>> kvar = tf.keras.backend.ones((3,4))
  >>> tf.keras.backend.eval(kvar)
  array([[1.,  1.,  1.,  1.],
         [1.,  1.,  1.,  1.],
         [1.,  1.,  1.,  1.]], dtype=float32)

  """
with ops.init_scope():
    if dtype is None:
        dtype = floatx()
    tf_dtype = dtypes_module.as_dtype(dtype)
    v = array_ops.ones(shape=shape, dtype=tf_dtype, name=name)
    if py_all(v.shape.as_list()):
        exit(variable(v, dtype=dtype, name=name))
    exit(v)
