# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a broadcaster.

    Do not call directly.
    The source_shape, target_shape, and layer_broadcasters are converted
    to have the same dtype.

    Note: source_shape.rank and target_shape.rank must be known.
    Args:
      source_shape: the source DynamicRaggedShape
      target_shape: the target DynamicRaggedShape
      layer_broadcasters: List[_LayerBroadcaster] of length source_shape.rank.
      dtype: the preferred dtype of the broadcaster.

    Raises:
      TypeError: if the input types don't match.
    """
if not isinstance(source_shape, DynamicRaggedShape):
    raise TypeError("source_shape is not a DynamicRaggedShape")
if not isinstance(target_shape, DynamicRaggedShape):
    raise TypeError("target_shape is not a DynamicRaggedShape")
if not isinstance(layer_broadcasters, list):
    raise TypeError("layer_broadcasters not a list: " +
                    str(layer_broadcasters))
for bc in layer_broadcasters:
    if not isinstance(bc, _LayerBroadcaster):
        raise TypeError("Not a LayerBroadcaster: " + str(bc))

dtype = _find_dtype(source_shape, dtype)
dtype = _find_dtype(target_shape, dtype)
dtype = _find_dtype_iterable(layer_broadcasters, dtype)
dtype = _find_dtype(dtypes.int64, dtype)
self._source_shape = source_shape.with_dtype(dtype)
self._target_shape = target_shape.with_dtype(dtype)
self._layer_broadcasters = [x.with_dtype(dtype) for x in layer_broadcasters]
