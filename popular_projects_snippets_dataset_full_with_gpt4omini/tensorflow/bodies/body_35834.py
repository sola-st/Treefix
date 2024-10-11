# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError, "empty"):
        variables.PartitionedVariable(
            name="fail",
            shape=2,
            dtype=dtypes.int32,
            variable_list=[],
            partitions=[])

    with self.assertRaisesRegex(ValueError, "must have a save_slice_info"):
        v0 = variables.Variable([0])
        partitions = [1]
        variables.PartitionedVariable(
            name="two_vars",
            shape=[1],
            dtype=v0.dtype,
            variable_list=[v0],
            partitions=partitions)

    with self.assertRaisesRegex(ValueError, "full shapes must match"):
        v0 = variables.Variable([0])
        v1 = variables.Variable([1])
        v0._set_save_slice_info(
            variables.Variable.SaveSliceInfo(v0.name, [2], [0], [1]))
        v1._set_save_slice_info(
            variables.Variable.SaveSliceInfo(v0.name, [2], [1], [1]))
        partitions = [2]

        variables.PartitionedVariable(
            name="two_vars",
            shape=[3],
            dtype=v0.dtype,
            variable_list=[v1, v0],
            partitions=partitions)

    with self.assertRaisesRegex(ValueError, "must be positive"):
        v0 = variables.Variable([0])
        v0._set_save_slice_info(
            variables.Variable.SaveSliceInfo(v0.name, [2], [0], [1]))
        partitions = [0]

        variables.PartitionedVariable(
            name="two_vars",
            shape=[2],
            dtype=v0.dtype,
            variable_list=[v0],
            partitions=partitions)
