# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
i = variables.Variable([100] * 3, dtype=dtypes.int32, name="i")
j = constant_op.constant([20] * 3, dtype=dtypes.int32, name="j")
k = math_ops.add(i, j, name="k")

self.evaluate(variables.global_variables_initializer())
self.assertAllEqual([100] * 3, i)
self.assertAllEqual([120] * 3, k)
self.assertAllEqual([20] * 3, j)

with self.assertRaisesRegex(AssertionError, r"not equal lhs"):
    self.assertAllEqual([0] * 3, k)
