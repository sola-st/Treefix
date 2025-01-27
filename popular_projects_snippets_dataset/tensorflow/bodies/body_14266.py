# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
np.random.seed(42)
num_rows = 128
num_cols = 27
size = 1000
inp = np.random.randint(0, size, (num_rows, num_cols), dtype=dtype)
np_out = np.reshape(
    np.concatenate(
        [np.bincount(inp[j, :], minlength=size) for j in range(num_rows)],
        axis=0), (num_rows, size))
x = ragged_tensor.RaggedTensor.from_tensor(inp)
self.assertAllEqual(
    np_out,
    self.evaluate(bincount_ops.bincount(arr=x, minlength=size, axis=-1)))
