# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(2, 2, 2, 2))
b = array_ops.placeholder(np.float32, shape=(4, 4, 4, 2))

dim_nums = xla_data_pb2.DotDimensionNumbers()
dim_nums.lhs_contracting_dimensions.append(2)
dim_nums.rhs_contracting_dimensions.append(3)
dim_nums.lhs_batch_dimensions.append(0)
dim_nums.rhs_batch_dimensions.append(0)

with self.assertRaisesRegex(ValueError,
                            'Dimensions must be equal, but are 2 and 4'):
    xla.dot_general(a, b, dim_nums)
