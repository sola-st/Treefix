# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
# This test was added after discovering a memory allocation bug in the GPU
# kernel that the existing tests did not catch due to being too small.
for n in [250, 2500, 25000]:
    indices = np.zeros([n, 2], dtype=np.int64)
    indices[:, 0] = np.arange(n)
    values = np.zeros([n], dtype=np.float32)
    dense_shape = np.array([n, 3], dtype=np.int64)
    sp_input = sparse_tensor.SparseTensor(indices, values, dense_shape)
    sp_tensors = self.evaluate(
        sparse_ops.sparse_split(sp_input=sp_input, num_split=2, axis=0))
    self.assertAllEqual(sp_tensors[0].indices, indices[:n // 2])
    self.assertAllEqual(sp_tensors[1].indices, indices[n // 2:] - [n // 2, 0])
    self.assertAllEqual(sp_tensors[0].values, values[:n // 2])
    self.assertAllEqual(sp_tensors[1].values, values[n // 2:])
    self.assertAllEqual(sp_tensors[0].dense_shape, [n // 2, 3])
    self.assertAllEqual(sp_tensors[1].dense_shape, [n // 2, 3])
