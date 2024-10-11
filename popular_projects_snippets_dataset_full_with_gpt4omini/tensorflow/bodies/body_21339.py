# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# slot_creator is used only in optimizer V1.
# We insert our own custom split XLA sharding that overrides the SPMD
# sharding copied over by the slot_creator.
with ops.Graph().as_default(), self.cached_session():
    v = variables.Variable([1.0, 2.5, 10.0, 15.1], name="var")
    v = xla_sharding.mesh_split(
        v, np.array([0, 1]), [0], use_sharding_op=False)
    with ops.control_dependencies(None):
        slot = slot_creator.create_zeros_slot(
            v, name="slot", dtype=dtypes.float64, copy_xla_sharding=True)
        slot = xla_sharding.split(
            slot, split_dimension=0, num_devices=4, use_sharding_op=False)

    self.assertNotEqual(
        xla_sharding.get_tensor_sharding(v),
        xla_sharding.get_tensor_sharding(slot))

    slot_sharding = xla_sharding.get_tensor_sharding(slot)
    slot_proto = xla_data_pb2.OpSharding()
    slot_proto.ParseFromString(slot_sharding)
    self.assertEqual(
        slot_proto,
        xla_data_pb2.OpSharding(
            type=xla_data_pb2.OpSharding.OTHER,
            tile_assignment_dimensions=[4],
            tile_assignment_devices=range(4)))
