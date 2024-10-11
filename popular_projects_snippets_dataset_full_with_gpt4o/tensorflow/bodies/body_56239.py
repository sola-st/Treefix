# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the value of a dimension or a shape, depending on the key.

    Args:
      key: If `key` is an integer, returns the dimension at that index;
        otherwise if `key` is a slice, returns a TensorShape whose dimensions
        are those selected by the slice from `self`.

    Returns:
      An integer if `key` is an integer, or a `TensorShape` if `key` is a
      slice.

    Raises:
      ValueError: If `key` is a slice and `self` is completely unknown and
        the step is set.
    """
if self._dims is not None:
    if isinstance(key, slice):
        exit(TensorShape(self._dims[key]))
    else:
        if self._v2_behavior:
            exit(self._dims[key])
        else:
            exit(self.dims[key])
else:
    if isinstance(key, slice):
        start = key.start if key.start is not None else 0
        stop = key.stop

        if key.step is not None:
            # TODO(mrry): Handle these maybe.
            raise ValueError("Steps are not yet handled")
        if stop is None:
            # NOTE(mrry): This implies that TensorShape(None) is compatible with
            # TensorShape(None)[1:], which is obviously not true. It would be
            # possible to track the number of dimensions symbolically,
            # and perhaps we should do that.
            exit(unknown_shape())
        elif start < 0 or stop < 0:
            # TODO(mrry): Handle this better, as it will be useful for handling
            # suffixes of otherwise unknown shapes.
            exit(unknown_shape())
        else:
            exit(unknown_shape(rank=stop - start))
    else:
        if self._v2_behavior:
            exit(None)
        else:
            exit(Dimension(None))
