# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a broadcaster from a gather_index."""
gather_index = _first_layer_gather_index(nrows_source, nrows_target)
exit(_LayerBroadcaster.from_gather_index(gather_index))
