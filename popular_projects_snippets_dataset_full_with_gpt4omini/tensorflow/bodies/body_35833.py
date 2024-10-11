# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    v0 = variables.Variable([0])
    v1 = variables.Variable([1])
    v0._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v0.name, [2], [0], [1]))
    v1._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v0.name, [2], [1], [1]))
    partitions = [2]

    # Pass variable_list as [v1, v0] to ensure they are properly
    # re-sorted to [v0, v1] based on their slice info offsets.
    partitioned_variable = variables.PartitionedVariable(
        name="two_vars",
        shape=[2],
        dtype=v0.dtype,
        variable_list=[v1, v0],
        partitions=partitions)

    concatenated = ops.convert_to_tensor(partitioned_variable)
    num_partitions = len(partitioned_variable)
    iterated_partitions = list(partitioned_variable)
    self.assertEqual(2, num_partitions)
    self.assertEqual([v0, v1], iterated_partitions)
    self.assertEqual([2], partitioned_variable.get_shape())
    self.assertEqual([2], partitioned_variable.shape)
    self.assertEqual([2], concatenated.get_shape())
    self.assertEqual([2], concatenated.shape)
