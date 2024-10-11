# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dynamic_partition_op_test.py
for seg_dtype in [dtypes.int32, dtypes.int64]:
    data_tensor = ragged_factory_ops.constant(
        data, row_splits_dtype=seg_dtype, ragged_rank=data_ragged_rank)
    segment_ids_tensor = ragged_factory_ops.constant(
        partitions,
        dtype=seg_dtype,
        row_splits_dtype=seg_dtype,
        ragged_rank=segment_ids_ragged_rank)
    expected_tensor = ragged_factory_ops.constant(
        expected,
        row_splits_dtype=seg_dtype,
        ragged_rank=expected_ragged_rank)
    result = ragged_array_ops.stack_dynamic_partitions(
        data_tensor, segment_ids_tensor, num_partitions)
    self.assertAllEqual(result, expected_tensor)

    # Check that it's equivalent to tf.stack(dynamic_partition(...)),
    # where applicable.
    if (data_ragged_rank == 0 and segment_ids_ragged_rank == 0 and
        seg_dtype == dtypes.int32):
        equiv = ragged_concat_ops.stack(
            data_flow_ops.dynamic_partition(data_tensor, segment_ids_tensor,
                                            num_partitions))
        self.assertAllEqual(result, self.evaluate(equiv).to_list())
