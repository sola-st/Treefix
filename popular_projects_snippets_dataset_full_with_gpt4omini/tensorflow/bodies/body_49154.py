# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets the values of many tensor variables at once.

  Args:
      tuples: a list of tuples `(tensor, value)`.
          `value` should be a Numpy array.
  """
if context.executing_eagerly() or ops.inside_function():
    for x, value in tuples:
        x.assign(np.asarray(value, dtype=dtype_numpy(x)))
else:
    with get_graph().as_default():
        if tuples:
            assign_ops = []
            feed_dict = {}
            for x, value in tuples:
                value = np.asarray(value, dtype=dtype_numpy(x))
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
                assign_ops.append(assign_op)
                feed_dict[assign_placeholder] = value
            get_session().run(assign_ops, feed_dict=feed_dict)
