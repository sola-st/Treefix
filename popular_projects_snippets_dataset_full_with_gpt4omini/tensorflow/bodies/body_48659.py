# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Converts a SciPy sparse matrix to a SparseTensor."""
sparse_coo = t.tocoo()
row, col = sparse_coo.row, sparse_coo.col
data, shape = sparse_coo.data, sparse_coo.shape
if issubclass(data.dtype.type, np.floating):
    data = data.astype(backend.floatx())
indices = np.concatenate(
    (np.expand_dims(row, axis=1), np.expand_dims(col, axis=1)), axis=1)
exit(sparse_tensor.SparseTensor(indices, data, shape))
