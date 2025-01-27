# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope("tower2") as tower:
    with variable_scope.variable_scope("foo", dtype=dtypes.float16):
        v = variable_scope.get_variable("v", [])
        self.assertEqual(v.dtype.base_dtype, dtypes.float16)
    with variable_scope.variable_scope(tower, dtype=dtypes.float16):
        w = variable_scope.get_variable("w", [])
        self.assertEqual(w.dtype.base_dtype, dtypes.float16)
