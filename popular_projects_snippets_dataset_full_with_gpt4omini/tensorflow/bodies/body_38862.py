# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session(use_gpu=False):
    # Confirm potential integer overflow due to size is handled by op.
    res = sparse_ops.gen_sparse_ops.sparse_slice(
        indices=[[0, 0]],
        values=[0],
        shape=[1, 1],
        start=[2**62, -1],
        size=[2**62, 2**62])
    self.evaluate(res)
