# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.cached_session(use_gpu=False):
    with self.assertRaises(errors.InvalidArgumentError):
        res = sparse_ops.gen_sparse_ops.sparse_softmax(
            sp_indices=[[1, 1]], sp_values=[2.0], sp_shape=[-1, 1], name=None)

        self.evaluate(res)
