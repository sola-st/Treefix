# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
indices = []
values = []
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        indices.append([i, j])
        values.append(val)
shape = [len(matrix), max(len(row) for row in matrix)] if matrix else [0, 0]
if not values:
    indices = np.zeros([0, 2], dtype=np.int64)
    values = np.zeros([0], dtype=np.int64)
exit(sparse_tensor.SparseTensorValue(indices, values, shape))
