# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
input_sizes = constant_op.constant([4, 4, 4, 4, 4])
filter_input = stateless_random_ops.stateless_random_uniform(
    shape=[4, 4, 4, 4, 4], seed=[0, 1])
out_backprop = stateless_random_ops.stateless_random_uniform(
    shape=[4, 4, 4, 4, 4], seed=[0, 1])
strides = [1, 1, 1, 1, 1]

expected_result = gen_nn_ops.conv3d_backprop_input_v2(
    input_sizes=input_sizes,
    filter=filter_input,
    out_backprop=out_backprop,
    strides=strides,
    padding='SAME')

if shard_type == 'replicated':
    grad_layout = Layout.replicated(self.mesh, rank=5)
else:
    grad_layout = Layout.batch_sharded(self.mesh, self._mesh_dim_b, rank=5)

got_result = gen_nn_ops.conv3d_backprop_input_v2(
    input_sizes=numpy_util.pack_numpy(input_sizes,
                                      Layout.replicated(self.mesh, rank=1)),
    filter=numpy_util.pack_numpy(filter_input,
                                 Layout.replicated(self.mesh, rank=5)),
    out_backprop=numpy_util.pack_numpy(out_backprop, grad_layout),
    strides=strides,
    padding='SAME')

self.assertDTensorEqual(expected_result, grad_layout, got_result)
