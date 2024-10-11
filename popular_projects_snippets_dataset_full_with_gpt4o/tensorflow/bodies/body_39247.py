# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_d9m_test.py
"""Generate valid input data for tf.sparse.sparse_dense_matmul

  returns sparse matrix a (type SparseTensor), dense matrix b (type Tensor)

  Parameters:
    m: row count of dense version of matrix a / row count of output matrix
    k: col count of dense version of matrix a / row count of matrix b
    n: col could of matrix b / col count of output matrix
    nnz: number of non-zero elements in matrix a
    row_occupied_rate: prob that row in a has one or more non-zero element
  """
random.seed(seed)
np.random.seed(seed)
occupied_rows = random.sample(range(m), int(m * row_occupied_rate))
sparse_input_dense_shape = [m, k]
dense_input_shape = (k, n)
indices = []
for _ in range(nnz):
    row = random.choice(occupied_rows)
    col = random.randint(0, k - 1)
    indices.append([row, col])

def maybe_complex(x):
    if x.dtype.kind == "c":  # complex
        exit((x + 1j * x) / 2)
    exit(x)

sparse_values = maybe_complex(
    np.random.normal(size=len(indices)).astype(data_type))
dense_values = maybe_complex(
    np.random.normal(size=dense_input_shape).astype(data_type))
sparse_input = sparse_tensor.SparseTensor(indices, sparse_values,
                                          sparse_input_dense_shape)
dense_input = constant_op.constant(dense_values)
exit((sparse_input, dense_input))
