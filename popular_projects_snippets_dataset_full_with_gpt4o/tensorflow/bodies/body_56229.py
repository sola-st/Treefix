# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Creates a new TensorShape with the given dimensions.

    Args:
      dims: A list of Dimensions, or None if the shape is unspecified.

    Raises:
      TypeError: If dims cannot be converted to a list of dimensions.
    """
if isinstance(dims, (tuple, list)):  # Most common case.
    self._dims = tuple(as_dimension(d).value for d in dims)
elif dims is None:
    self._dims = None
elif isinstance(dims, tensor_shape_pb2.TensorShapeProto):
    if dims.unknown_rank:
        self._dims = None
    else:
        self._dims = tuple(
            # Protos store variable-size dimensions as -1
            dim.size if dim.size != -1 else None
            for dim in dims.dim
            )
elif isinstance(dims, TensorShape):
    self._dims = dims._dims
else:
    try:
        dims_iter = iter(dims)
    except TypeError:
        # Treat as a singleton dimension
        self._dims = (as_dimension(dims).value,)
    else:
        self._dims = []
        for d in dims_iter:
            try:
                self._dims.append(as_dimension(d).value)
            except TypeError as e:
                raise TypeError(
                    "Failed to convert '{0!r}' to a shape: '{1!r}'"
                    "could not be converted to a dimension. A shape should "
                    "either be single dimension (e.g. 10), or an iterable of "
                    "dimensions (e.g. [1, 10, None]).".format(dims, d)) from e
        self._dims = tuple(self._dims)
