# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
reverse_index_map = [0, 1]
grad_values = [[0, 1], [2, 3]]
# Note: Eager mode and graph mode throw different errors here. Graph mode
# will fail with a ValueError from the shape checking logic, while Eager
# will fail with an InvalidArgumentError from the kernel itself.
if context.executing_eagerly():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                r'grad_values must be a vector'):
        self.evaluate(
            gen_sparse_ops.SparseFillEmptyRowsGrad(
                reverse_index_map=reverse_index_map, grad_values=grad_values))
else:
    with self.assertRaisesRegex(ValueError,
                                r'Shape must be rank 1 but is rank 2'):
        self.evaluate(
            gen_sparse_ops.SparseFillEmptyRowsGrad(
                reverse_index_map=reverse_index_map, grad_values=grad_values))
