# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
num_rows = 128
num_cols = 27
size = 100
np.random.seed(42)
inp = np.random.randint(0, size, (num_rows, num_cols), dtype=dtype)
np_out = np.reshape(
    np.concatenate(
        [np.bincount(inp[j, :], minlength=size) for j in range(num_rows)],
        axis=0), (num_rows, size))
# from_dense will filter out 0s.
inp = inp + 1
# from_dense will cause OOM in GPU.
with ops.device("/CPU:0"):
    inp_sparse = sparse_ops.from_dense(inp)
    inp_sparse = sparse_tensor.SparseTensor(inp_sparse.indices,
                                            inp_sparse.values - 1,
                                            inp_sparse.dense_shape)
self.assertAllEqual(
    np_out, self.evaluate(bincount_ops.bincount(arr=inp_sparse, axis=-1)))
