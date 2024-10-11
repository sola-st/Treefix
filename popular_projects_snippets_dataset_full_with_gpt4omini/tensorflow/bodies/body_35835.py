# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session():
    v0 = variables.Variable(initial_value=[0.0])
    v1 = variables.Variable(initial_value=[1.0])
    v2 = variables.Variable(initial_value=[20.0])
    v3 = variables.Variable(initial_value=[30.0])
    v0._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v0.name, [2], [0], [1]))
    v1._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v1.name, [2], [1], [1]))
    v2._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v2.name, [2], [0], [1]))
    v3._set_save_slice_info(
        variables.Variable.SaveSliceInfo(v3.name, [2], [1], [1]))

    partitions = [2]

    # Pass variable_list as [v1, v0] to ensure they are properly
    # re-sorted to [v0, v1] based on their slice info offsets.
    pv_0 = variables.PartitionedVariable(
        name="two_vars",
        shape=[2],
        dtype=v0.dtype,
        variable_list=[v0, v1],
        partitions=partitions)

    pv_1 = variables.PartitionedVariable(
        name="two_vars",
        shape=[2],
        dtype=v0.dtype,
        variable_list=[v2, v3],
        partitions=partitions)

    deltas_a = constant_op.constant([1.0, 2.0])
    deltas_b = constant_op.constant([3.0, 4.0])
    ones = array_ops.ones([2])
    plus_delta = pv_0.assign_add(deltas_a)
    minus_delta = pv_0.assign_sub(deltas_b)
    assign_ones = pv_0.assign(ones)

    c_0 = constant_op.constant([2.0])
    c_1 = constant_op.constant([3.0])
    assign_list = pv_1.assign([c_0, c_1])
    assign_part_value = pv_1.assign_add(assign_ones)
    assign_part_var = pv_1.assign_sub(pv_0)
    self.evaluate(variables.global_variables_initializer())

    self.assertEqual([1.0], self.evaluate(plus_delta[0]))
    self.assertEqual([1.0], self.evaluate(v0))
    self.assertEqual([3.0], self.evaluate(plus_delta[1]))
    self.assertEqual([3.0], self.evaluate(v1))

    self.assertEqual([-2.0], self.evaluate(minus_delta[0]))
    self.assertEqual([-2.0], self.evaluate(v0))
    self.assertEqual([-1.0], self.evaluate(minus_delta[1]))
    self.assertEqual([-1.0], self.evaluate(v1))

    self.assertEqual([1.0], self.evaluate(assign_ones[0]))
    self.assertEqual([1.0], self.evaluate(v0))
    self.assertEqual([1.0], self.evaluate(assign_ones[1]))
    self.assertEqual([1.0], self.evaluate(v1))

    self.assertEqual([2.0], self.evaluate(assign_list[0]))
    self.assertEqual([2.0], self.evaluate(v2))
    self.assertEqual([3.0], self.evaluate(assign_list[1]))
    self.assertEqual([3.0], self.evaluate(v3))

    self.assertEqual([3.0], self.evaluate(assign_part_value[0]))
    self.assertEqual([3.0], self.evaluate(v2))
    self.assertEqual([4.0], self.evaluate(assign_part_value[1]))
    self.assertEqual([4.0], self.evaluate(v3))

    self.assertEqual([2.0], self.evaluate(assign_part_var[0]))
    self.assertEqual([2.0], self.evaluate(v2))
    self.assertEqual([3.0], self.evaluate(assign_part_var[1]))
    self.assertEqual([3.0], self.evaluate(v3))
