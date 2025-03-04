# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
reverse_index_map = [2, -1]
grad_values = [0, 1, 2, 3]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r'Elements in reverse index must be in \[0, 4\)'):
    self.evaluate(
        gen_sparse_ops.SparseFillEmptyRowsGrad(
            reverse_index_map=reverse_index_map, grad_values=grad_values))
