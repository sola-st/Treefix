# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16_test.py
"""Test if requested dtype is honored in the getter.
    """
with bfloat16.bfloat16_scope() as scope:
    v1 = variable_scope.get_variable("v1", [])
    self.assertEqual(v1.dtype.base_dtype, dtypes.float32)
    v2 = variable_scope.get_variable("v2", [], dtype=dtypes.bfloat16)
    self.assertEqual(v2.dtype.base_dtype, dtypes.bfloat16)
    self.assertEqual([dtypes.float32, dtypes.float32],
                     [v.dtype.base_dtype for v in scope.global_variables()])
