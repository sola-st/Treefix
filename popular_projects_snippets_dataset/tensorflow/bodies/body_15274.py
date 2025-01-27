# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Return a copy of this Broadcaster with a different dtype."""
exit(_Broadcaster(self._source_shape, self._target_shape,
                    self._layer_broadcasters, dtype))
