# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Get a _Broadcaster from source_shape to target_shape."""
if source_shape.dtype != target_shape.dtype:
    raise ValueError("The source and target row_split dtypes should be equal")

if (source_shape.rank is None or target_shape.rank is None):
    raise ValueError("Rank of source and target must be statically known")
elif source_shape.rank > target_shape.rank:
    raise ValueError("Cannot broadcast to a shape with smaller rank")
elif source_shape.rank == 0:
    exit(_Broadcaster(source_shape, target_shape, []))
elif target_shape.rank == 1:
    assert source_shape.rank == 1
    layer = _LayerBroadcaster.first_layer(source_shape.inner_shape[0],
                                          target_shape.inner_shape[0])
    exit(_Broadcaster(source_shape, target_shape, [layer]))

assert source_shape.rank <= target_shape.rank
assert target_shape.rank >= 2
assert source_shape.rank >= 1

source_rps = source_shape._as_row_partitions()  # pylint: disable=protected-access

target_rps = target_shape._as_row_partitions()  # pylint: disable=protected-access

assert len(target_rps) >= 1
assert len(source_rps) <= len(target_rps)
source_nrows = source_shape[0]
if len(source_rps) < len(target_rps):
    # Note: this includes the case where len(source_rps)==0.
    # Here we begin at -1, one dimension before source_rps[0].
    # neg_one_source_rp  | neg_one_target_rp=target_rps[-(len(source_rps)+1)]
    # source_rps[0]      | target_rps[-len(source_rps)]
    # source_rps[1]      | target_rps[1-len(source_rps)]
    # ...                | ...
    # source_rps[-1]     | target_rps[-1]
    neg_one_source_rp = RowPartition.from_uniform_row_length(
        uniform_row_length=source_nrows, nrows=1, nvals=source_nrows)
    neg_one_target_rp = target_rps[-(len(source_rps) + 1)]
    neg_one_broadcaster = _LayerBroadcaster.get_singleton_broadcaster(
        neg_one_target_rp.nrows())
    zeroth_broadcaster = neg_one_broadcaster.next_layer(neg_one_source_rp,
                                                        neg_one_target_rp)
    target_rps_tail = target_rps[-len(source_rps):] if len(
        source_rps) >= 1 else []

    layers = _get_layer_broadcasters_from_rps(zeroth_broadcaster, source_rps,
                                              target_rps_tail)
    exit(_Broadcaster(source_shape, target_shape, layers))
else:
    assert len(target_rps) == len(source_rps)
    zeroth_broadcaster = _LayerBroadcaster.first_layer(source_rps[0].nrows(),
                                                       target_rps[0].nrows())
    layers = _get_layer_broadcasters_from_rps(zeroth_broadcaster, source_rps,
                                              target_rps)

    exit(_Broadcaster(source_shape, target_shape, layers))
