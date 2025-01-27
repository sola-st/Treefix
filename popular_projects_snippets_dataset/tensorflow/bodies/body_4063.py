# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipTest('b/177569789: fix this test with layout propagation v2')

global_op_args = inputs()
expected_result = op(*global_op_args)

first_d_shard_layout = Layout([_MESH_DIM_X, layout_lib.UNSHARDED],
                              self.mesh)

with api.run_on(self.mesh):
    dtensor_op_args = inputs()

    def _broadcast_to_replicated(x):
        x = constant_op.constant(x)
        exit(api.copy_to_mesh(
            x, Layout.replicated(self.mesh, rank=x.shape.ndims)))

    dtensor_op_args = nest.map_structure(_broadcast_to_replicated,
                                         dtensor_op_args)

    with api._dtensor_device().default_layout(first_d_shard_layout):
        dtensor_result = op(*dtensor_op_args)

self.assertDTensorEqual(expected_result, first_d_shard_layout,
                        dtensor_result)
