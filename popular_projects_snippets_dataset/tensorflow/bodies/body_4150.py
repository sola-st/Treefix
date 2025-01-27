# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tensor_layout = self.layouts[tensor_dimension][2]
updates_layout = self.layouts[updates_dimension][indices_rank]

# Tensor is shape [4, 2], indices is shape [..., 2, 1], updates is shape
# [..., 2, 2]
#
# Entries in indices should be unique and integers in the range [0, 4).
# Tensor and updates are float.

tensor_numpy = np.random.uniform(size=[4, 2])
padding_axes = [1] * (indices_rank - 2)
updates_numpy = np.random.uniform(size=padding_axes + [2, 2])
indices_numpy_flat = np.array(
    [np.random.randint(0, 4),
     np.random.randint(0, 3)])
if indices_numpy_flat[0] == indices_numpy_flat[1]:
    indices_numpy_flat[1] += 1
indices_numpy = indices_numpy_flat.reshape(padding_axes + [2, 1])

tensor = constant_op.constant(tensor_numpy, dtype=dtypes.float32)
updates = constant_op.constant(updates_numpy, dtype=dtypes.float32)
indices = constant_op.constant(indices_numpy, dtype=dtypes.int32)

golden_result = op_type(tensor=tensor, updates=updates, indices=indices)

tensor = numpy_util.pack_numpy(tensor, tensor_layout)
updates = numpy_util.pack_numpy(updates, updates_layout)
indices = numpy_util.pack_numpy(
    indices, Layout.replicated(tensor_layout.mesh, indices_rank))

dtensor_result = op_type(tensor=tensor, updates=updates, indices=indices)

# If either of the inputs are sharded in the non-index dimension, then
# the output is as well, otherwise it is replicated.
if tensor_dimension == 1 or updates_dimension == 1:
    expected_layout = self.layouts[1][2]
else:
    expected_layout = self.layouts[-1][2]

self.assertDTensorEqual(golden_result, expected_layout, dtensor_result)
