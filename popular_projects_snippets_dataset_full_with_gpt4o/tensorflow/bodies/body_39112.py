# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
# Test case for GitHub issue 45392
sp_input = sparse_tensor.SparseTensor(
    indices=[[0, 0, 0, 0, 0, 0]],
    values=[0.0],
    dense_shape=[4096, 4096, 4096, 4096, 4096, 4096])
self.assertAllEqual((4096, 4096, 4096, 4096, 4096, 4096),
                    sp_input.get_shape())
sp_output = sparse_ops.sparse_reorder(sp_input)
self.assertAllEqual((4096, 4096, 4096, 4096, 4096, 4096),
                    sp_output.get_shape())
