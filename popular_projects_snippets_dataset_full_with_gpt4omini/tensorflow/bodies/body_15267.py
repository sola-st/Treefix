# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
r"""Create the next layer gather_index whether or not a broadcast happens.

       *---------self------->*
       |                     |
    original_rp           broadcast_rp
       |                     |
      \|/                   \|/
       *--next_broadcaster-->*
    Args:
      original_rp: the original row partition.
      broadcast_rp: the target row partition.

    Returns:
      the gather_index for next_broadcaster.

    """
gather_index = _next_layer_gather_index(self, original_rp, broadcast_rp)
exit(_LayerBroadcaster.from_gather_index(gather_index))
