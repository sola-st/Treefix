# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session():
    with self.assertRaises(errors.InvalidArgumentError):
        sp_output = sparse_ops.gen_sparse_ops.sparse_reshape(
            input_indices=[[0, 0]],
            input_shape=[2**32, 2**31],
            new_shape=[1, 1],
            name=None)

        self.evaluate(sp_output)
