# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
# The SPMD sharding annotations should not be copied since the primary
# variable and slot variable have different ranks.
with ops.Graph().as_default(), self.cached_session():
    v = variables.Variable([1.0, 2.5], name="var")
    v = xla_sharding.mesh_split(
        v, np.array([0, 1]), [0], use_sharding_op=False)
    with ops.control_dependencies(None):
        slot = slot_creator.create_slot(
            v,
            constant_op.constant(10, name="const"),
            name="slot",
            copy_xla_sharding=True)
    self.assertIsNone(xla_sharding.get_tensor_sharding(slot))
    self.assertNotEqual(
        xla_sharding.get_tensor_sharding(v),
        xla_sharding.get_tensor_sharding(slot))
