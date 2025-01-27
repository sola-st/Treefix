# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    grad, _ = self.evaluate(
        sparse_ops.sparse_fill_empty_rows_grad(
            reverse_index_map=[], grad_values=[]))
    self.assertAllEqual(grad, [])
