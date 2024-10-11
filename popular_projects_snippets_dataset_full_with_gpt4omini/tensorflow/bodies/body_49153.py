# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets the value of a variable, from a Numpy array.

  `backend.set_value` is the complement of `backend.get_value`, and provides
  a generic interface for assigning to variables while abstracting away the
  differences between TensorFlow 1.x and 2.x semantics.

  {snippet}

  Args:
      x: Variable to set to a new value.
      value: Value to set the tensor to, as a Numpy array
          (of the same shape).
  """
value = np.asarray(value, dtype=dtype_numpy(x))
if ops.executing_eagerly_outside_functions():
    x.assign(value)
else:
    with get_graph().as_default():
        tf_dtype = dtypes_module.as_dtype(x.dtype.name.split('_')[0])
        if hasattr(x, '_assign_placeholder'):
            assign_placeholder = x._assign_placeholder
            assign_op = x._assign_op
        else:
            # In order to support assigning weights to resizable variables in
            # Keras, we make a placeholder with the correct number of dimensions
            # but with None in each dimension. This way, we can assign weights
            # of any size (as long as they have the correct dimensionality).
            placeholder_shape = tensor_shape.TensorShape([None] * value.ndim)
            assign_placeholder = array_ops.placeholder(
                tf_dtype, shape=placeholder_shape)
            assign_op = x.assign(assign_placeholder)
            x._assign_placeholder = assign_placeholder
            x._assign_op = assign_op
        get_session().run(assign_op, feed_dict={assign_placeholder: value})
