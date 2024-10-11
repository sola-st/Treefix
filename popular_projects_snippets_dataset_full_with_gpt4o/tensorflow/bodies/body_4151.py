# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['GPU'], 'b/179387248 cases with AllConcat crash')
params_layout = self.layouts[params_dimension][3]
indices_layout = self.layouts[indices_dimension][2]

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

params = numpy_util.pack_numpy(params, params_layout)
indices = numpy_util.pack_numpy(indices, indices_layout)

dtensor_result = gen_array_ops.gather_nd(params=params, indices=indices)

if params_dimension < 2 and indices_dimension == 0:
    # if params isn't sharded in the last dimension, then sharding of indices
    # the first dimension gives a first dimension sharding of the output
    expected_layout = self.layouts[0][2]
elif params_dimension == 2:
    # if params is sharded in the last dimension, then sharding of indices is
    # ignored as they are both sharded on the same dimension.
    expected_layout = self.layouts[1][2]
else:
    expected_layout = self.layouts[-1][2]

self.assertDTensorEqual(golden_result, expected_layout, dtensor_result)
