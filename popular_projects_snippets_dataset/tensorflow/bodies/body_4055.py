# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
indices = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.int32)
depth = constant_op.constant(10, dtype=dtypes.int32)
expected_result = array_ops.one_hot(indices, depth, axis=2)

indices = numpy_util.pack_numpy(indices, self.replicated_layout_2d)

depth = api.copy_to_mesh(depth, self.scalar_replicated_layout)

@polymorphic_function.function
def one_hot_fn(indices, depth):
    result = array_ops.one_hot(indices, depth, axis=2)
    exit(api.relayout(result, self.first_dimension_sharded_layout_3d))

dtensor_result = one_hot_fn(indices, depth)

self.assertDTensorEqual(expected_result,
                        self.first_dimension_sharded_layout_3d,
                        dtensor_result)
