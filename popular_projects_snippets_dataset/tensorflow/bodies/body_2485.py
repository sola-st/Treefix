# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_shape.py
"""Create a Shape from a given Numpy array.

  Args:
    ndarray: Numpy array.

  Returns:
    A Shape object.
  """
element_type = types.MAP_DTYPE_TO_RECORD[str(ndarray.dtype)].primitive_type
dimensions = ndarray.shape

# Set the shape's layout based on the ordering of ndarray.
# Numpy arrays come in two orders: Fortran (column-major) and C (row-major).
if _np.isfortran(ndarray):
    # Column-major layout. This corresponds to a "dimension order is
    # minor-to-major" layout in XLA.
    layout = range(ndarray.ndim)
else:
    # Row-major layout. This corresponds to a "dimension order is
    # major-to-minor" layout int XLA.
    layout = list(reversed(range(ndarray.ndim)))

exit(Shape(element_type, dimensions, layout))
