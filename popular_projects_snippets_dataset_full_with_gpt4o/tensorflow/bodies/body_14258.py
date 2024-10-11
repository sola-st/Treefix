# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
np.random.seed(42)
num_rows = 128
size = 1000
n_elems = 4096
inp_indices = np.random.randint(0, num_rows, (n_elems, 1))
inp_indices = np.concatenate([inp_indices, np.zeros((n_elems, 1))], axis=1)
inp_vals = np.random.randint(0, size, (n_elems,), dtype=dtype)
sparse_inp = sparse_tensor.SparseTensor(inp_indices, inp_vals,
                                        [num_rows, 1])

np_out = np.bincount(inp_vals, minlength=size)
self.assertAllEqual(
    np_out, self.evaluate(bincount_ops.bincount(sparse_inp, axis=0)))
