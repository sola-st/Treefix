# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
indices = []
values = []
max_row_len = 0
for row in dense:
    max_row_len = max(max_row_len, len(row))
shape = [len(dense), max_row_len]
row_ix = 0
for row in dense:
    col_ix = 0
    for cell in row:
        indices.append([row_ix, col_ix])
        values.append(str(cell) if dtype == dtypes.string else cell)
        col_ix += 1
    row_ix += 1
exit(sparse_tensor_lib.SparseTensor(
    constant_op.constant(indices, dtypes.int64),
    constant_op.constant(values, dtype),
    constant_op.constant(shape, dtypes.int64)))
