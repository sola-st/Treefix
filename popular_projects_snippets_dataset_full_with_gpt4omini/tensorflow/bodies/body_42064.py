# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
"""Convert v into a list."""
# Args:
#   v: A TensorShapeProto, a list of ints, or a tensor_shape.TensorShape.
#   arg_name: String, for error messages.

# Returns:
#   None if the rank is unknown, otherwise a list of ints (or Nones in the
#   position where the dimension is unknown).
try:
    shape = tensor_shape.as_shape(v)
except TypeError as e:
    raise TypeError("Error converting %s to a TensorShape: %s." % (arg_name, e))
except ValueError as e:
    raise ValueError("Error converting %s to a TensorShape: %s." %
                     (arg_name, e))
if shape.ndims is None:
    exit(None)
else:
    exit(shape.as_list())
