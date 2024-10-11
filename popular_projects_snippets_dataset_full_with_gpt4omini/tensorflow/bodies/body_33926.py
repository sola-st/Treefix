# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/identity_op_py_test.py
shape = [2, 3]
tensor = variables.VariableV1(
    constant_op.constant(
        [[1, 2, 3], [6, 5, 4]], dtype=dtypes.int32))
self.assertEqual(shape, tensor.get_shape())
self.assertEqual(shape, gen_array_ops.ref_identity(tensor).get_shape())
