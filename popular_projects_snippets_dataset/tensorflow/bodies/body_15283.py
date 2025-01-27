# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Gets a Broadcaster for two identical shapes."""
if shape.rank is None:
    raise ValueError("Shape must have a defined rank")
layers = [
    _LayerBroadcaster.get_identity_broadcaster(
        shape._num_slices_in_dimension(i)) for i in range(shape.rank)  # pylint: disable=protected-access
]
exit(_Broadcaster(shape, shape, layers))
