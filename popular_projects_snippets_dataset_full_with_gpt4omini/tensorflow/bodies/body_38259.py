# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
np.random.seed(42)
num_rows = 128
size = 10
n_elems = 4096
inp_indices = np.random.randint(0, num_rows, (n_elems, 1))
inp_vals = np.random.randint(0, size, (n_elems,), dtype=dtype)

np_out = np.ones((size,))
self.assertAllEqual(
    np_out,
    self.evaluate(
        gen_math_ops.sparse_bincount(
            indices=inp_indices,
            values=inp_vals,
            dense_shape=[num_rows],
            size=size,
            weights=[],
            binary_output=True)))
