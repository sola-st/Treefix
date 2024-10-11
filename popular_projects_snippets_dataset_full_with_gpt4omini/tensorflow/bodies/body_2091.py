# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(2, 3, 4))
b = array_ops.placeholder(np.float32, shape=(None, 4))

dim_nums = xla_data_pb2.DotDimensionNumbers()
dim_nums.lhs_contracting_dimensions.append(2)
dim_nums.rhs_contracting_dimensions.append(1)
dim_nums.lhs_batch_dimensions.append(0)
dim_nums.rhs_batch_dimensions.append(0)

c = xla.dot_general(a, b, dim_nums)
self.assertEqual(c.shape.as_list(), [2, 3])
