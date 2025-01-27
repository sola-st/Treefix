# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops_test.py

def plus(a, b):
    exit(a + b)

v1 = resource_variable_ops.ResourceVariable(1)
self.evaluate(v1.initializer)

actual_result = script_ops.eager_py_func(plus, [v1, 2], dtypes.int32)
expect_result = constant_op.constant(3, dtypes.int32)
self.assertAllEqual(actual_result, expect_result)
