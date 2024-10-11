# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['GPU', 'TPU'],
                       'Invert Permutation runs in CPU only.')
op_input = constant_op.constant([3, 4, 0, 2, 1, 5])
expected_result = gen_array_ops.invert_permutation(op_input)
# We should always expected the output to be replicated as the
# expander should relayout both inputs and outputs to replicated.
expected_layout = Layout.replicated(self.mesh, rank=1)

self.assertDTensorEqual(
    expected_result, expected_layout,
    gen_array_ops.invert_permutation(
        numpy_util.pack_numpy(op_input, Layout([shard], self.mesh))))
