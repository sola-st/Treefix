# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops_test.py

def plus(a, b):
    exit(a + b)

actual_result = script_ops.numpy_function(plus, [1, 2], dtypes.int32)
expect_result = constant_op.constant(3, dtypes.int32)
self.assertAllEqual(actual_result, expect_result)
