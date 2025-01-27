# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(1, 2, 3, 4))
b = array_ops.placeholder(np.float32, shape=(4, 5, 2, 6))

dim_nums = xla_data_pb2.DotDimensionNumbers()
dim_nums.lhs_contracting_dimensions.append(1)
dim_nums.rhs_contracting_dimensions.append(2)
dim_nums.lhs_batch_dimensions.append(3)
dim_nums.rhs_batch_dimensions.append(0)

c = xla.dot_general(a, b, dim_nums)
self.assertEqual(c.shape, tensor_shape.TensorShape([4, 1, 3, 5, 6]))
