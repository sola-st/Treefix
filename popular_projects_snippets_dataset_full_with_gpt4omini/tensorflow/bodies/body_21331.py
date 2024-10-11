# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.cached_session():
    v = random_ops.random_uniform([2], dtype=dtypes.float64)
    v = array_ops.placeholder_with_default(v, shape=[None], name="const")
    with ops.control_dependencies(None):
        slot = slot_creator.create_zeros_slot(
            v, name="slot", dtype=dtypes.float64)

    self.evaluate(variables.global_variables_initializer())

    self.assertEqual("const/slot", slot.op.name)
    self.assertEqual([2], array_ops.shape(slot).eval())
    self.assertEqual(dtypes.float64, slot.dtype.base_dtype)
    self.assertAllEqual([0.0, 0.0], self.evaluate(slot))
