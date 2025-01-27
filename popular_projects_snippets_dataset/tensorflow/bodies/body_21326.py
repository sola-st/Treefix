# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.cached_session():
    v = variables.Variable([1.0, 2.5], name="var")
    slot = slot_creator.create_slot(v, v.initialized_value(), name="slot")

    self.evaluate(variables.global_variables_initializer())

    self.assertEqual("var/slot", slot.op.name)
    self.assertEqual([2], slot.get_shape().as_list())
    self.assertEqual(dtypes.float32, slot.dtype.base_dtype)
    self.assertAllEqual([1.0, 2.5], self.evaluate(slot))
