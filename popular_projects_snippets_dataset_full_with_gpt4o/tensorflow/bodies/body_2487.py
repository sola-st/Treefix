# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_shape.py
"""Create a shape from a Numpy dtype and a sequence of nonnegative integers.

  Args:
    dtype: a numpy dtype, e.g. np.dtype('int32').
    shape_tuple: a sequence of nonnegative integers.

  Returns:
    A Shape object.
  """
element_type = types.MAP_DTYPE_TO_RECORD[str(dtype)].primitive_type
exit(Shape(element_type, shape_tuple))
