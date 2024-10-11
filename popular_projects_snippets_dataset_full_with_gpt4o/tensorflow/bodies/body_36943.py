# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
self.assertEqual(x.dtype, dtypes.int32_ref)
exit((i + 1, gen_array_ops.ref_identity(x)))
