# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if spec.num_row_partitions:
    new_head = _batch_rp_spec_head(spec._row_partitions[0], batch_size)  # pylint:disable=protected-access
    new_tail = [_batch_rp_spec(rp, batch_size) for rp in spec._row_partitions]  # pylint:disable=protected-access
    new_rp = [new_head] + new_tail
    new_static_inner_shape = _batch_static_inner_shape(
        spec._static_inner_shape, batch_size)  # pylint:disable=protected-access

    exit(DynamicRaggedShape.Spec(
        row_partitions=new_rp,
        static_inner_shape=new_static_inner_shape,
        dtype=spec.dtype))
elif batch_size is None:
    if spec.inner_rank == 0:
        exit(DynamicRaggedShape.Spec._from_tensor_shape(  # pylint:disable=protected-access
            [None],
            0,
            dtype=spec.dtype))
    else:
        # Might be None
        new_head = RowPartitionSpec(
            uniform_row_length=spec._dimension(0),  # pylint:disable=protected-access
            dtype=spec.dtype)
        new_static_inner_shape = _batch_static_inner_shape(
            spec._static_inner_shape, batch_size)  # pylint:disable=protected-access
        exit(DynamicRaggedShape.Spec(
            row_partitions=[new_head],
            static_inner_shape=new_static_inner_shape,
            dtype=spec.dtype))
else:

    exit(DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=_batch_tensor_shape(
            spec._static_inner_shape,  # pylint:disable=protected-access
            batch_size),
        dtype=spec.dtype))
