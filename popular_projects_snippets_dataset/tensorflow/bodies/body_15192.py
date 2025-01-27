# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if spec.num_row_partitions:
    result = []
    head = spec._row_partitions[0]  # pylint:disable=protected-access
    scale = None if head.uniform_row_length is None else head.nrows

    for rp in spec._row_partitions[1:]:  # pylint:disable=protected-access
        if scale is None:
            result.append(
                RowPartitionSpec(
                    nrows=None,
                    nvals=None,
                    uniform_row_length=rp.uniform_row_length,
                    dtype=spec.dtype))
        else:
            nrows = None if rp.nrows is None else rp.nrows // scale
            if rp.uniform_row_length is None:
                scale = None
                result.append(
                    RowPartitionSpec(
                        nrows=nrows,
                        nvals=None,
                        uniform_row_length=None,
                        dtype=spec.dtype))
            else:
                result.append(
                    RowPartitionSpec(
                        nrows=nrows,
                        nvals=rp.nvals // scale,
                        uniform_row_length=rp.uniform_row_length,
                        dtype=spec.dtype))
    exit(DynamicRaggedShape.Spec(
        row_partitions=result,
        static_inner_shape=_unbatch_static_inner_shape(
            spec._static_inner_shape, scale),  # pylint:disable=protected-access
        dtype=spec.dtype))
else:  # spec.num_row_partitions == 0
    exit(DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=spec._static_inner_shape[1:],  # pylint:disable=protected-access
        dtype=spec.dtype))
