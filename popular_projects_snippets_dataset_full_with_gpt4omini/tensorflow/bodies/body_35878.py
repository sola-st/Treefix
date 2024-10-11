# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    # Partitioning a variable of shape=[2048] with a minimum of 2K per slice.
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=2 << 10,
        var_name="v0_0",
        var_shape=[2048],
        expected_axis_shards=4,
        expected_partitions=[4])

    # Partitioning a variable of shape=[2048, 1024] with a minimum of 256K per
    # slice.
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=256 << 10,
        var_name="v0",
        var_shape=[2048, 1024],
        expected_axis_shards=32,
        expected_partitions=[32, 1])

    # max_partitions restricts partitioning of the variable.
    self._testMinMaxVariablePartitioner(
        max_partitions=16,
        axis=0,
        min_slice_size=256 << 10,
        var_name="v1_max",
        var_shape=[2048, 1024],
        expected_axis_shards=16,
        expected_partitions=[16, 1])
    self._testMinMaxVariablePartitioner(
        max_partitions=1,
        axis=0,
        min_slice_size=256 << 10,
        var_name="v2_max",
        var_shape=[2048, 1024],
        expected_axis_shards=1,
        expected_partitions=[1, 1])

    # Reducing/Increasing min_slice_size proportionately increases/reduces the
    # number of partitions.
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=128 << 10,
        var_name="v3_slice",
        var_shape=[2048, 1024],
        expected_axis_shards=64,
        expected_partitions=[64, 1])
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=512 << 10,
        var_name="v4_slice",
        var_shape=[2048, 1024],
        expected_axis_shards=16,
        expected_partitions=[16, 1])

    # Partitioning the variable along a different axis.
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=1,
        min_slice_size=256 << 10,
        var_name="v5_axis",
        var_shape=[64, 1024, 1, 3],
        expected_axis_shards=3,
        expected_partitions=[1, 3, 1, 1])
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=3,
        min_slice_size=256 << 10,
        var_name="v6_axis",
        var_shape=[64, 1024, 1, 3],
        expected_axis_shards=3,
        expected_partitions=[1, 1, 1, 3])

    # Can not partition the variable more than what its shape allows.
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=256 << 10,
        var_name="v7_shape",
        var_shape=[16, 128, 1024],
        expected_axis_shards=16,
        expected_partitions=[16, 1, 1])
    self._testMinMaxVariablePartitioner(
        max_partitions=100,
        axis=0,
        min_slice_size=256 << 10,
        var_name="v8_shape",
        var_shape=[4, 512, 1024],
        expected_axis_shards=4,
        expected_partitions=[4, 1, 1])
