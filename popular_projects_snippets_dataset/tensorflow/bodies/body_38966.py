# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.cached_session(use_gpu=False):
    with self.assertRaises(errors.InvalidArgumentError):
        res = sparse_ops.gen_sparse_ops.sparse_reduce_max(
            input_indices=[[1, 2], [3, 4]],
            input_shape=[2**32, 2**31],
            input_values=[1, 3],
            reduction_axes=[0],
            keep_dims=False,
            name=None)

        self.evaluate(res)
    with self.assertRaises(errors.InvalidArgumentError):
        res = sparse_ops.gen_sparse_ops.sparse_reduce_max_sparse(
            input_indices=[[1, 2], [3, 4]],
            input_shape=[2**32, 2**31],
            input_values=[1, 3],
            reduction_axes=[0],
            keep_dims=False,
            name=None)

        self.evaluate(res)
    with self.assertRaises(errors.InvalidArgumentError):
        res = sparse_ops.gen_sparse_ops.sparse_reduce_sum(
            input_indices=[[1, 2], [3, 4]],
            input_shape=[2**32, 2**31],
            input_values=[1, 3],
            reduction_axes=[0],
            keep_dims=False,
            name=None)

        self.evaluate(res)
