# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
i = variables.Variable([100], dtype=dtypes.int32, name="i")
j = constant_op.constant([20], dtype=dtypes.int32, name="j")
k = math_ops.add(i, j, name="k")

self.evaluate(variables.global_variables_initializer())
self.assertNotAllEqual([100] * 3, i)
self.assertNotAllEqual([120] * 3, k)
self.assertNotAllEqual([20] * 3, j)

with self.assertRaisesRegex(
    AssertionError, r"two values are equal at all elements. $"):
    self.assertNotAllEqual([120], k)

with self.assertRaisesRegex(
    AssertionError, r"two values are equal at all elements.*extra message"):
    self.assertNotAllEqual([120], k, msg="extra message")
