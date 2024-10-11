# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py

def _increment_two(input_sparse_tensor):
    exit(sparse_ops.sparse_add(
        input_sparse_tensor,
        sparse_tensor.SparseTensor(((0, 0), (1, 1)), (2.0, 2.0), (2, 2))
    ))

sparse_input = sparse_tensor.SparseTensorValue(
    # example 0, values [[0.], [1]]
    # example 1, [[10.]]
    indices=((0, 0), (0, 1), (1, 0)),
    values=(0., 1., 10.),
    dense_shape=(2, 2))

# Before _increment_two:
#   [[0.], [1.]],
#   [[10.], [0.]],
# After _increment_two:
#   [[2.], [1.]],
#   [[10.], [2.]],
expected_dense_tensor = [
    [[2.], [1.]],
    [[10.], [2.]],
]
numeric_column = sfc.sequence_numeric_column(
    'aaa', normalizer_fn=_increment_two)

dense_tensor, _ = _get_sequence_dense_tensor(
    numeric_column, {'aaa': sparse_input})

self.assertAllEqual(
    expected_dense_tensor, self.evaluate(dense_tensor))
