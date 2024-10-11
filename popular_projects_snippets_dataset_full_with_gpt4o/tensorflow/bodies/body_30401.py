# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
indices = constant_op.constant([[0], [1], [2]], dtypes.int64)
values = constant_op.constant(np.array([1, 2, 3], np.int64))
shape = constant_op.constant([3], dtypes.int64)
st = sparse_tensor.SparseTensor(indices, values, shape)
st_cast = math_ops.cast(st, dtypes.float32)

self.assertAllEqual(st_cast.indices, [[0], [1], [2]])
self.assertAllEqual(st_cast.values,
                    np.array([1, 2, 3], np.float32))
self.assertAllEqual(st_cast.dense_shape, [3])
