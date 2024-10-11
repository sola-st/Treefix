# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.test_session():
    s = variables.Variable(1.0, name="var")
    p_v = variable_scope.get_variable(
        "var",
        shape=[2, 2],
        partitioner=partitioned_variables.fixed_size_partitioner(2))
    for i, v in enumerate(p_v):
        slot = slot_creator.create_slot(v, s.initialized_value(), name="slot")

        self.evaluate(variables.global_variables_initializer())

        self.assertEqual("var/part_%d/slot" % i, slot.op.name)
        self.assertEqual([], slot.get_shape().as_list())
        self.assertEqual(dtypes.float32, slot.dtype.base_dtype)
        self.assertAllEqual(1.0, slot)
