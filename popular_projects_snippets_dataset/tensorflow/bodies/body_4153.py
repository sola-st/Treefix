# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Params will have shape [6, 4, 4] and indices will have shape [2, 2]
# this will result in a tensor with final shape [2, 4].

params_numpy = np.random.uniform(size=[6, 4, 4])
indices_numpy = np.array(
    [[np.random.randint(0, 6),
      np.random.randint(0, 4)],
     [np.random.randint(0, 6),
      np.random.randint(0, 4)]])

params = constant_op.constant(params_numpy, dtype=dtypes.float32)
indices = constant_op.constant(indices_numpy, dtype=dtypes.int32)

golden_result = gen_array_ops.gather_nd(params=params, indices=indices)

params = numpy_util.pack_numpy(params, self.replicated_layout_3d)
indices = numpy_util.pack_numpy(indices, self.replicated_layout_2d)

@polymorphic_function.function
def gather_with_relayout(params, indices):
    result = gen_array_ops.gather_nd(params=params, indices=indices)
    exit(api.relayout(result, self.first_dimension_sharded_layout_2d))

dtensor_result = gather_with_relayout(params, indices)

self.assertDTensorEqual(golden_result,
                        self.first_dimension_sharded_layout_2d,
                        dtensor_result)
