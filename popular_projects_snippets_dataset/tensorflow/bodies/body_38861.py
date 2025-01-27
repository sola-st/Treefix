# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_slice_op_test.py
with self.session(use_gpu=False):
    with self.assertRaises(errors.InvalidArgumentError):
        res = sparse_ops.gen_sparse_ops.sparse_slice(
            indices=[[0, 0]],
            values=[0],
            shape=[1, 1],
            start=[10, 10],
            size=[-100, 100])
        self.evaluate(res)
