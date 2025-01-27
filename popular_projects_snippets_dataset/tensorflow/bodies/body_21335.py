# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.cached_session():
    v = variables.Variable([1.0, 2.5], name="var")
    v = xla_sharding.mesh_split(
        v, np.array([0, 1]), [0], use_sharding_op=False)
    slot = slot_creator.create_slot(
        v, v.initialized_value(), name="slot", copy_xla_sharding=True)
    self.assertEqual(
        xla_sharding.get_tensor_sharding(v),
        xla_sharding.get_tensor_sharding(slot))
