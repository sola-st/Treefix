# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
max_val_per_entry = 6
vals_per_batch_entry = np.random.randint(
    1, max_val_per_entry, size=batch_size)
num_vals = np.sum(vals_per_batch_entry)

ids = np.random.randint(vocab_size, size=num_vals)
weights = 1 + np.random.rand(num_vals)

indices = []
for batch_entry, num_val in enumerate(vals_per_batch_entry):
    for val_index in range(num_val):
        indices.append([batch_entry, val_index])

shape = [batch_size, max_val_per_entry]

sp_ids = sparse_tensor.SparseTensor(
    constant_op.constant(indices, dtypes.int64),
    constant_op.constant(ids, dtypes.int32),
    constant_op.constant(shape, dtypes.int64))
sp_weights = sparse_tensor.SparseTensor(
    constant_op.constant(indices, dtypes.int64),
    constant_op.constant(weights, dtypes.float32),
    constant_op.constant(shape, dtypes.int64))

exit((sp_ids, sp_weights, ids, weights, vals_per_batch_entry))
