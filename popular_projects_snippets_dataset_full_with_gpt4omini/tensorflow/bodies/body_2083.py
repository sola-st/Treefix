# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(4, 4, 4, 4))
b = array_ops.placeholder(np.float32, shape=(4, 4, 4, 4))

dim_nums = xla_data_pb2.DotDimensionNumbers()
dim_nums.lhs_contracting_dimensions.append(2)
dim_nums.rhs_contracting_dimensions.append(2)
dim_nums.rhs_contracting_dimensions.append(3)

with self.assertRaisesRegex(ValueError,
                            'Must specify the same number of contracting '
                            'dimensions for lhs and rhs. Got: 1 and 2'):
    xla.dot_general(a, b, dim_nums)
