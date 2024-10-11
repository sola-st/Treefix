# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.cached_session():
    dyn_shape = constant_op.constant([2], dtype=dtypes.int32)
    dyn_shape = array_ops.placeholder_with_default(dyn_shape,
                                                   shape=[None])
    v = variable_scope.get_variable(
        "var",
        initializer=random_ops.random_uniform(dyn_shape,
                                              dtype=dtypes.float64),
        validate_shape=False)
    with ops.control_dependencies(None):
        slot = slot_creator.create_zeros_slot(
            v, name="slot", dtype=dtypes.float64)

    self.evaluate(variables.global_variables_initializer())

    self.assertEqual("var/slot", slot.op.name)
    self.assertEqual([2], array_ops.shape(slot).eval())
    self.assertEqual(dtypes.float64, slot.dtype.base_dtype)
    self.assertAllEqual([0.0, 0.0], self.evaluate(slot))
