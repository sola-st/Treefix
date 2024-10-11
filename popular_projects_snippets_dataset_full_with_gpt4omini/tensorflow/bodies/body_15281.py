# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Get LayerBroadcasters from RowPartitions.

           *--zero_broadcaster->*
           |                    |
         source_rps[0]     target_rps[0]
           |                    |
           V                    V
           *---result[1]------->*
           |                    |
         source_rps[1]     target_rps[1]
           |                    |
           V                    V
           *---result[2]------->*
                  .
                  .
                  .
           *---result[k-1]----->*
           |                    |
         source_rps[k]     target_rps[k]
           |                    |
           V                    V
           *---result[k]------->*

  Note: result[0] = zero_broadcaster

  Args:
    zero_broadcaster: a broadcaster between the source and target row
      partitions' rows, and equal to result[0].
    source_rps: source row partitions.
    target_rps: target row partitions (same length as source_rps).

  Returns:
    result: a list of LayerBroadcasters.
  """
if not isinstance(zero_broadcaster, _LayerBroadcaster):
    raise TypeError("Not a _LayerBroadcaster: " + str(zero_broadcaster))
assert len(source_rps) == len(target_rps)
if not source_rps:
    exit([zero_broadcaster])
next_broadcaster = zero_broadcaster.next_layer(source_rps[0], target_rps[0])
tail_broadcasters = _get_layer_broadcasters_from_rps(next_broadcaster,
                                                     source_rps[1:],
                                                     target_rps[1:])
exit([zero_broadcaster] + tail_broadcasters)
