# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = example(
    features=features({
        # FixLen features
        "c": float_feature([3, 4]),
        "d": float_feature([0.0, 1.0]),
        # Sparse features
        "val": bytes_feature([b"a", b"b"]),  # for sp
        "idx": int64_feature([0, 3]),  # for sp
        "st_a": float_feature([3.0, 4.0]),
        # Ragged features
        "rt_1d": float_feature([3.0, 4.0]),
        "rt_values": float_feature([5, 6, 7]),  # for rt_2d
        "rt_splits": int64_feature([0, 1, 1, 3]),  # for rt_2d
        "rt_lengths": int64_feature([1, 0, 2]),  # for rt_2d
        "rt_starts": int64_feature([0, 1, 1]),  # for rt_2d
        "rt_limits": int64_feature([1, 1, 3]),  # for rt_2d
        "rt_rowids": int64_feature([0, 2, 2]),  # for rt_2d
        "rt_splits2": int64_feature([0, 2, 3]),  # for rt_3d
    }))
serialized = original.SerializeToString()

a_default = [1, 2, 3]
b_default = np.random.rand(3, 3).astype(bytes)
test_features = {
    "st_a":
        parsing_ops.VarLenFeature(dtypes.float32),
    "sp":
        parsing_ops.SparseFeature(["idx"], "val", dtypes.string, [13]),
    "a":
        parsing_ops.FixedLenFeature((1, 3),
                                    dtypes.int64,
                                    default_value=a_default),
    "b":
        parsing_ops.FixedLenFeature((3, 3),
                                    dtypes.string,
                                    default_value=b_default),
    # Feature "c" must be provided, since it has no default_value.
    "c":
        parsing_ops.FixedLenFeature(2, dtypes.float32),
    "d":
        parsing_ops.FixedLenSequenceFeature([],
                                            dtypes.float32,
                                            allow_missing=True),
    "rt_1d":
        parsing_ops.RaggedFeature(dtypes.float32),
    "rt_2d_with_splits":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowSplits("rt_splits")],
            dtype=dtypes.float32),
    "rt_2d_with_lengths":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowLengths("rt_lengths")],
            dtype=dtypes.float32),
    "rt_2d_with_starts":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowStarts("rt_starts")],
            dtype=dtypes.float32),
    "rt_2d_with_limits":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowLimits("rt_limits")],
            dtype=dtypes.float32),
    "rt_2d_with_rowids":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.ValueRowIds("rt_rowids")],
            dtype=dtypes.float32),
    "rt_2d_with_uniform_row_length":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.UniformRowLength(1)],
            dtype=dtypes.float32),
    "rt_3d":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[
                parsing_ops.RaggedFeature.RowSplits("rt_splits2"),
                parsing_ops.RaggedFeature.RowSplits("rt_splits")
            ],
            dtype=dtypes.float32),
    "rt_3d_with_uniform_row_length":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[
                parsing_ops.RaggedFeature.UniformRowLength(1),
                parsing_ops.RaggedFeature.RowSplits("rt_splits")
            ],
            dtype=dtypes.float32),
}

expected_st_a = (
    np.array([[0], [1]], dtype=np.int64),  # indices
    np.array([3.0, 4.0], dtype=np.float32),  # values
    np.array([2], dtype=np.int64))  # shape: max_values = 2

expected_sp = (  # indices, values, shape
    np.array([[0], [3]], dtype=np.int64), np.array(["a", "b"], dtype="|S"),
    np.array([13], dtype=np.int64))  # max_values = 13

expected_rt_1d = constant_op.constant([3, 4], dtypes.float32)

expected_rt_2d = ragged_factory_ops.constant([[5], [], [6, 7]],
                                             dtype=dtypes.float32)

expected_rt_2d_uniform = constant_op.constant([[5], [6], [7]],
                                              dtype=dtypes.float32)

expected_rt_3d = ragged_factory_ops.constant([[[5], []], [[6, 7]]],
                                             dtype=dtypes.float32)

expected_rt_3d_with_uniform = (
    ragged_tensor.RaggedTensor.from_uniform_row_length(
        expected_rt_2d, uniform_row_length=1))

expected_output = {
    "st_a": expected_st_a,
    "sp": expected_sp,
    "a": [a_default],
    "b": b_default,
    "c": np.array([3, 4], dtype=np.float32),
    "d": np.array([0.0, 1.0], dtype=np.float32),
    "rt_1d": expected_rt_1d,
    "rt_2d_with_splits": expected_rt_2d,
    "rt_2d_with_lengths": expected_rt_2d,
    "rt_2d_with_starts": expected_rt_2d,
    "rt_2d_with_limits": expected_rt_2d,
    "rt_2d_with_rowids": expected_rt_2d,
    "rt_2d_with_uniform_row_length": expected_rt_2d_uniform,
    "rt_3d": expected_rt_3d,
    "rt_3d_with_uniform_row_length": expected_rt_3d_with_uniform,
}

self._test(
    {
        "example_names": ops.convert_to_tensor("in1"),
        "serialized": ops.convert_to_tensor(serialized),
        "features": test_features,
    }, expected_output)
