# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    # Create a partitioned variable of shape (4, 8, 16, 32) type float32
    # Bytes per slice along the given axes:

    # 8 * 16 * 32 * sizeof(float32) = 16384 / slice on axis 0
    # 4 * 16 * 32 * sizeof(float32) = 8192 / slice on axis 1
    # 4 * 8 * 32 * sizeof(float32) = 4096 / slice on axis 2
    # 4 * 8 * 16 * sizeof(float32) = 2048 / slice on axis 3

    # Now partition it in different ways...

    # No need to slice: bytes_per_slice * dim0 = 65536 < max_shard_bytes
    self._testVariableAxisSizePartitioner(
        "v0",
        axis=0,
        max_shard_bytes=131072,
        expected_axis_shards=1,
        expected_partitions=(1, 1, 1, 1))

    # Slice exactly once: bytes_per_slice * dim1 = 65536 = max_shard_bytes
    self._testVariableAxisSizePartitioner(
        "v1",
        axis=1,
        max_shard_bytes=65536,
        expected_axis_shards=1,
        expected_partitions=(1, 1, 1, 1))

    # Slice into 2 parts:
    # bytes_per_slice = 4096
    # slices_per_shard = 32768 / 4096 = 8
    # axis_shards = 16 / 8 = 2
    self._testVariableAxisSizePartitioner(
        "v2",
        axis=2,
        max_shard_bytes=32768,
        expected_axis_shards=2,
        expected_partitions=(1, 1, 2, 1))

    # This partitioner makes sure we maximize the number of shards along
    # axis 3. Slice it into 32 parts:
    # bytes_per_slice = 2048
    # slices_per_shard = 2048 / 2048 = 1
    # axis_shards = 32 / 1 = 32
    self._testVariableAxisSizePartitioner(
        "v3a",
        axis=3,
        max_shard_bytes=2048,
        expected_axis_shards=32,
        expected_partitions=(1, 1, 1, 32))

    # This partitioner makes sure we do not go past the bound of allowable
    # number of shards along axis 3.
    # Slice into 32 parts:
    # bytes_per_slice = 2048
    # slices_per_shard = max(1, 1024 / 2048) = 1
    # axis_shards = 32 / 1 = 32
    # Slice into max of 32 parts because: max_shard_bytes < bytes_per_slice
    self._testVariableAxisSizePartitioner(
        "v3b",
        axis=3,
        max_shard_bytes=1024,
        expected_axis_shards=32,
        expected_partitions=(1, 1, 1, 32))

    # Specify max_shards so that it won't affect sharding.
    self._testVariableAxisSizePartitioner(
        "v3c",
        axis=3,
        max_shard_bytes=1024,
        expected_axis_shards=32,
        expected_partitions=(1, 1, 1, 32),
        max_shards=33)

    # Specify max_shards so that it will affect sharding.
    self._testVariableAxisSizePartitioner(
        "v3d",
        axis=3,
        max_shard_bytes=1024,
        expected_axis_shards=2,
        expected_partitions=(1, 1, 1, 2),
        max_shards=2)

    # Use the partitioner with strings
    partitioner_axis3_str = partitioned_variables.variable_axis_size_partitioner(  # pylint: disable=line-too-long
        axis=3,
        max_shard_bytes=32768,
        bytes_per_string_element=8)

    with variable_scope.variable_scope(
        "root", partitioner=partitioner_axis3_str):
        v3str = variable_scope.get_variable(
            "v3str",
            initializer=np.array([""] * 4 * 8 * 16 * 32).reshape(4, 8, 16, 32),  # pylint: disable=too-many-function-args
            dtype=dtypes.string,
            shape=(4, 8, 16, 32))
        v3str_list = v3str._get_variable_list()
        v3str_part = v3str._get_partitions()

        # Now the estimated bytes_per_slice = 4*8*16*bytes_per_string_element
        # which is equal to 4096.  Setting a max_shard_bytes of 32768
        # and we should get a split of 4.
        # Slice into 4 parts:
        # bytes_per_slice = 4096
        # slices_per_shard = 32768 / 4096 = 8
        # axis_shards = 32 / 8 = 4
        self.assertEqual(len(v3str_list), 4)
        self.assertAllEqual(v3str_part, (1, 1, 1, 4))
