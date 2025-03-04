# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
reverse_index_map = [2, 1]
grad_values = [0, 1, 2, 3]
d_values, d_default_value = self.evaluate(
    gen_sparse_ops.SparseFillEmptyRowsGrad(
        reverse_index_map=reverse_index_map, grad_values=grad_values))
self.assertAllEqual([2, 1], d_values)
self.assertEqual(3, d_default_value)
